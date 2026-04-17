from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional
from enum import Enum
from fastapi import Response
from fastapi import status
from typing import Annotated


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


@app.get("/annotatedeg/name")
def read_root(name:Annotated[str, 'this is just a metadata']) -> str:
    #return FileResponse(BASE_DIR / "static/view.html")
    # names = name
    return f'this is the input -> {name} an example of Type Hints with Metadata Annotations'


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

@app.put("/UpdStudent/id")
def updateStudent(id: int = 1, name: str = "this is the name"):
    """
    Update the name of a student by ID.

    Args:
        id (int): Student ID
        name (str): New name for the student

    Returns:
        dict: Updated student object

    Raises:
        ValueError: If student not found or invalid input
    """

    # ✅ Validate input
    if not isinstance(id, int):
        raise ValueError("Invalid ID: must be an integer")

    if not name or not isinstance(name, str):
        raise ValueError("Invalid name: must be a non-empty string")

    # ✅ Get student index
    index = getStudentIndex(id)

    if index is None or index >= len(students):
        raise ValueError(f"Student with id {id} not found")

    # ✅ Fetch student
    student = students[index]

    # ✅ Validate student structure
    if not isinstance(student, dict) or "id" not in student:
        raise ValueError("Invalid student data format")

    # ✅ Update logic (same as your original behavior)
    if student["id"] == id:
        student["name"] = name

    return student

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

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/itemsOptional/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/itemsReqDefOpt/{item_id}")    #define some parameters as required, some as having a default value, and some entirely optional
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

class Item(BaseModel):
    name: str = "name"
    description: str | None = None
    price: float
    tax: float | None = None

@app.post("/itemm/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/itemm/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

@app.get("/itemsQParamStrVal/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results