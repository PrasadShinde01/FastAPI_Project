from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional


app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool
    rating : Optional[int] = None

# Define the base directory for HTML files
BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
def read_root():
    #return FileResponse(BASE_DIR / "static/view.html")
    return {'this is FastAPI app!!!!'}

markss = '[12,23,13,13,31,31]'
@app.get("/marks/{i}")
async def marksare(i):
    k = type(i)
    print('......................',k)
    print('......................', type(i))  # Debugging the type of 'i'
    print('Type of markss:', type(markss))  # Debugging the
    return markss



@app.get("/egapi/{i}")
async def egapi(i):
    k = 10 
    return k


@app.get("/path")
def pathtest():
    return{"this is the path test"}


@app.post("/postp")
def pathtest():
    return{"this is the path test"}



@app.post("/paylb")
async def egapi(payload: dict = Body(...)):
    print(payload)
    print("the type of payload is :",type(payload))
    k = 10 
    return {f"title is : {payload["title"]} and content is {payload["content"]}"}

@app.post("/createPosts")
async def egapi(post: Post):
    print(post)
    print("the type of payload is :",type(post))
    k = 10 
    print('pydantic ',post)
   # print('dictionary method',post.model_dump())

    #print(Post.dict())
    #return {f"this is the title {post.title} return sstatement and Rating is {post.rating}"}
    #return("data":post.model_dump())
    return{"data":post}  

students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 16,
        "grade": "10th",
        "marks": 88
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 15,
        "grade": "9th",
        "marks": 92
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 17,
        "grade": "11th",
        "marks": 81
    }
]
#

@app.get("/postss/{id}")
def getStud(id:int):
    return(f"this is the data at index{id}", students[id])