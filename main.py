from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional
from enum import Enum
from fastapi import Response
from fastapi import status


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

markss = '[12,23,13,13,31]'
marksList = [12,23,13,13,31]
@app.get("/marks/{i}")
async def marksare(i):
    k = type(i)
    print('......................',k)
    print('......................', type(i))  # Debugging the type of 'i'
    print('Type of markss:', type(markss))  # Debugging the
    return markss


@app.get("/marksSum/{i}")
async def marksare(i):
    sumIs = sum(markss)
    return sumIs

@app.get("/Maxmarks/")
async def marksare():
    maxMarks = max(marksList)
    print('max marks in list:',maxMarks)
    return maxMarks

@app.get("/MinMarks/")
async def marksare():
    minMarks = min(marksList)
    print('min marks in list:',minMarks)
    return minMarks

@app.get("/revList/")
async def marksare():
    revList = list(reversed(marksList))
    print('min marks in list:',revList)
    return revList


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

class ItemGrosseries(str, Enum):
    SoyaChunks =  "Soyachunks"
    SoyaOil =  "SoyaOil"
    SoyaMilk =  "Soyamilk"

@app.get("/Grosseries/{itemGrosseries}")
async def itemGrosseries(itemGrosseries:ItemGrosseries):
    if itemGrosseries is ItemGrosseries.SoyaChunks:
        return {f"this itme is Soyachunks"}
    if itemGrosseries is ItemGrosseries.SoyaOil:
        return(f"this itme is SoyaOil")
    if itemGrosseries is ItemGrosseries.SoyaMilk:
        return(f"this itme is Soyamilk")

@app.get("/Grosseries/json/{itemGrosseries}")
async def itemGrosseries(itemGrosseries:ItemGrosseries):
    if itemGrosseries.value == "Soyachunks" :
        return {"itemGrosseries":itemGrosseries,"message":"this is some kind of message"}
    if itemGrosseries is ItemGrosseries.SoyaOil:
        return(f"this itme is SoyaOil")
    # return {"model_name": itemGrosseries, "message": "Have some residuals"}

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
#####################3

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/item/{id}")
async def itemId(id:int):
    return {"id is ":id}

@app.get("/itemss/{name}")
async def itemName(name:str):
    return {"the name is ":name}

@app.get("/item/defaultId")
async def itemId(id:int):
    return {f"this is the default id 1111"}
    #eturn(f"this is the data at index{id}", students[id])

def getStudentId(n):
    for i in students:
        if i["id"] == n:   # ✅ FIXED
            return i
    return None

@app.get("/studentdata/{id}")
async def studentByID(id: int, response: Response):
    student = getStudentId(id)
    print(students)
    if not student:
        response.status_code = 404
        print(f"post with {id} does not exist")
    #print(student)
    return student

def getStudentIndex(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            return index
    return None


@app.delete("/delStudentBy/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delStudentByID(id:int):
    index = getStudentIndex(id)
    if index == None:   
        raise HTTPException(status_code=status.HTTP_204_NOT_FOUND,detail= f"student wwith {id} not exist")
    students.pop(index)
    print(students)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/UpdStudent/id")
async def updateStudent(id:int,name:str):
    index = getStudentIndex(id)
    std = students[index] 
    print(std)
    print('students typeeeee',type(students))
    if std["id"]== id:
        std["name"] = name 
    print('updated std>>>>', std)
    return std

# @app.post("/AddStudent/id")
# async def updateStudent(id:int,name:str, age:int, grade:str,marks:int):
#     new_student = {
#         "id": id,
#         "name": name,
#         "age": age,
#         "grade": grade,
#         "marks": marks
#     }
#     students.append(new_student)
#     # res = Response(status_code=status.HTTP_204_NO_CONTENT)
#     return Response(new_student, status_code=status.HTTP_201_CREATED) 


@app.post("/AddStudent/{id}")
async def updateStudent(id: int, name: str, age: int, grade: str, marks: int):
    new_student = {
        "id": id,
        "name": name,
        "age": age,
        "grade": grade,
        "marks": marks
    }
    students.append(new_student)
    
    return JSONResponse(content=new_student, status_code=status.HTTP_201_CREATED)

# print(students)
# print(type(students))