from uuid import UUID, uuid4, uuid5, NAMESPACE_DNS
from fastapi import FastAPI, Path, HTTPException
import random
from fastapi_pagination import Page, add_pagination, paginate
import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
from pydantic import BaseModel, AfterValidator, Field, HttpUrl
from fastapi.params import Body
from typing import Literal, Optional
from enum import Enum
from fastapi import Response
from fastapi import status, Query
from typing import Annotated
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

app = FastAPI(
    title="UUID API",
    description="Simple API to generate, validate, and inspect UUIDs",
    version="1.0.0",
)

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

@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    item: Annotated[Item, Body(embed=True)],
    q: str | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.get("/itemsQFixVal/")
async def read_items(q: Annotated[str, Query(min_length=2, max_lenght = 50)] = "fixed query"):   
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



@app.get("/itemsQNoneVal/")
async def read_items(q: Annotated[str | None, Query(min_length=2, max_lenght = 50)]):   
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        print("this is now type", type(q))
        results.update({"q": q})
    return results

@app.get("/itemsNonetype/")
async def read_items(q: Annotated[str | None, Query(min_length=3)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    # if q:
    print("this is now type", type(q))
    results.update({"q": q})
    return results


@app.get("/itemsQListtype/")
async def read_items(q: Annotated[list[str] | None, Query(min_length=3)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    # if q:
    print("this is now type", type(q))
    results.update({"q": q})
    return results

@app.get("/itemslistparam/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

@app.get("/itemsQdescription/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


@app.get("/itemsAfterValidation/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item}

class FilterParams(BaseModel):
    limit: int = Field(100, gt=110, le=1100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/itemsFilterQuery/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query



with open('C:/Users/Prasad/fastapi_project/data/data.json') as f:
    data = json.load(f)

data_length = len(data)

@app.get('/data/posts')
def get_data():
    return data

@app.get('/data/Pagination')
def get_data(start_page:int = 1, end_page:int= 10):
    start = (start_page-1) * end_page
    end = start + end_page
    print(f'{start} start value and end is{end}')
    dt = data['posts']
    return dt[start:end]


@app.get("/data/fastpagination", response_model=Page[dict])
def get_data():
    return paginate(data["posts"])

# Important
add_pagination(app)


class ItemSet(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/itemsList/{item_id}")
async def update_item(item_id: int, itemList: ItemSet):
    results = {"item_id": item_id, "item": itemList}
    return results



class Image(BaseModel):
    url: HttpUrl
    name: str


class ItemImg(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[ItemImg]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

class OrderItem(BaseModel):
    product_name: str
    quantity: int
    unit_price: Decimal          # Decimal input → float in JSON response
    discount_percent: float = 0.0

class OrderRequest(BaseModel):
    customer_name: str
    items: list[OrderItem]
    order_date: datetime         # Accepts ISO string → parsed to datetime object
    voucher_id: UUID | None = None  # Accepts UUID string → parsed to UUID object

class OrderResponse(BaseModel):
    order_id: UUID               # UUID object → serialized to string in response
    customer_name: str
    items: list[OrderItem]
    order_date: datetime         # datetime object → serialized to ISO string in response
    subtotal: float
    discount_total: float
    final_total: float
    processed_at: datetime       # Auto-generated server-side datetime
    status: str

@app.post("/orders/create", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderRequest):
    """
    Demonstrates Data Conversion (Parsing + Serialization):

    PARSING (input):
      - "unit_price": "19.99"   →  Decimal("19.99")
      - "order_date": "2024-01-15T10:30:00"  →  datetime object
      - "voucher_id": "550e8400-e29b-41d4-a716..."  →  UUID object

    SERIALIZATION (output):
      - UUID   →  "3f6c1b2a-..." string
      - datetime  →  "2024-01-15T10:30:00" ISO string
      - Decimal   →  19.99 float
      - Computed float fields  →  rounded JSON numbers
    """

    # Pydantic already parsed and validated all input types
    subtotal = sum(
        float(item.unit_price) * item.quantity
        for item in order.items
    )

    discount_total = sum(
        float(item.unit_price) * item.quantity * (item.discount_percent / 100)
        for item in order.items
    )

    final_total = round(subtotal - discount_total, 2)

    return OrderResponse(
        order_id=uuid4(),                    # UUID → serialized to string
        customer_name=order.customer_name,
        items=order.items,
        order_date=order.order_date,         # datetime → serialized to ISO string
        subtotal=round(subtotal, 2),
        discount_total=round(discount_total, 2),
        final_total=final_total,
        processed_at=datetime.now(),         # Server-generated datetime
        status="confirmed"
    )

#  Declare Request Example Data Extra JSON Schema Data in Pydantic Models

class BookOrder(BaseModel):
    """
    Demonstrates both topics together:
    - Field(title, description, gt, lt) → Extra JSON Schema data
    - Field(example=...) → per-field example data
    - model_config with json_schema_extra → whole-body example + custom schema keywords
    """

    # --- Extra JSON Schema data: title, description, constraints ---
    book_title: str = Field(
        title="Book Title",
        description="Full title of the book being ordered",
        min_length=2,
        max_length=200,
        example="The Pragmatic Programmer"
    )

    author: str = Field(
        title="Author Name",
        description="Full name of the book's author",
        example="David Thomas"
    )

    quantity: int = Field(
        title="Order Quantity",
        description="Number of copies to order. Must be between 1 and 100.",
        gt=0,    # gt/lt/ge/le all appear as constraints in the generated JSON Schema
        le=100,
        example=3
    )

    price_per_copy: float = Field(
        title="Price Per Copy (INR)",
        description="Unit price in Indian Rupees",
        gt=0.0,
        example=599.00
    )

    genre: Optional[str] = Field(
        default=None,
        title="Book Genre",
        description="Optional genre/category of the book",
        example="Technology"
    )

    # --- Extra JSON Schema: model-level config with custom keywords ---
    model_config = {
        "json_schema_extra": {
            # This appears as a complete example in Swagger UI's "Example Value"
            "example": {
                "book_title": "Clean Code",
                "author": "Robert C. Martin",
                "quantity": 2,
                "price_per_copy": 749.00,
                "genre": "Software Engineering"
            },
            # Custom keyword — not standard JSON Schema, but shows up in the raw schema
            "x-internal-category": "book-orders",
            "x-requires-login": True
        }
    }


@app.post(
    "/bookOrders/create",
    summary="Create a book order",
    description="Demonstrates **Request Example Data** and **Extra JSON Schema Data**. Check the schema tab in Swagger UI to see titles, descriptions, constraints, and examples.",
    tags=["Learning - Schema & Examples"]
)
async def create_book_order(
    # openapi_examples on Body() → multiple named examples in Swagger UI
    order: Annotated[
        BookOrder,
        Body(
            openapi_examples={
                "tech_book": {
                    "summary": "A technology book",
                    "description": "Ordering a popular programming book",
                    "value": {
                        "book_title": "The Pragmatic Programmer",
                        "author": "David Thomas",
                        "quantity": 3,
                        "price_per_copy": 599.00,
                        "genre": "Technology"
                    }
                },
                "fiction_book": {
                    "summary": "A fiction novel",
                    "description": "Ordering a bestselling novel",
                    "value": {
                        "book_title": "The Alchemist",
                        "author": "Paulo Coelho",
                        "quantity": 1,
                        "price_per_copy": 299.00,
                        "genre": "Fiction"
                    }
                },
                "bulk_order": {
                    "summary": "Bulk order (no genre)",
                    "description": "A large quantity order without a genre specified",
                    "value": {
                        "book_title": "Clean Code",
                        "author": "Robert C. Martin",
                        "quantity": 50,
                        "price_per_copy": 749.00
                    }
                }
            }
        )
    ]
):
    total = round(order.quantity * order.price_per_copy, 2)
    return {
        "message": "Book order created successfully",
        "order_details": order.model_dump(),
        "total_price_inr": total
    }

class UUIDRequest(BaseModel):
    name: str                   # used for uuid5 (name-based)
 
 
class UUIDResponse(BaseModel):
    uuid: str
    version: int
 
 
# ── Routes ────────────────────────────────────────────────────────────────────
 
@app.get(
    "/uuid/generate",
    response_model=UUIDResponse,
    summary="Generate a random UUID (v4)",
    tags=["UUID"],
)
def generate_uuid():
    """Generates a new random UUID version 4."""
    new_id = uuid4()
    return UUIDResponse(uuid=str(new_id), version=new_id.version)
 
 
@app.post(
    "/uuid/generate/named",
    response_model=UUIDResponse,
    summary="Generate a name-based UUID (v5)",
    tags=["UUID"],
)
def generate_named_uuid(body: UUIDRequest):
    """
    Generates a deterministic UUID version 5 from a name string.
    Same name always produces the same UUID.
    """
    named_id = uuid5(NAMESPACE_DNS, body.name)
    return UUIDResponse(uuid=str(named_id), version=named_id.version)
 
 
@app.get(
    "/uuid/validate/{uuid}",
    summary="Validate a UUID string",
    tags=["UUID"],
)
def validate_uuid(
    uuid: str = Path(description="UUID string to validate"),
):
    """Checks whether the given string is a valid UUID and returns its details."""
    try:
        parsed = UUID(uuid)
        return {
            "valid": True,
            "uuid": str(parsed),
            "version": parsed.version,
            "int": parsed.int,
            "hex": parsed.hex,
            "urn": parsed.urn,
        }
    except ValueError:
        raise HTTPException(status_code=400, detail=f"'{uuid}' is not a valid UUID")
 
 
@app.get(
    "/uuid/batch",
    summary="Generate multiple UUIDs at once",
    tags=["UUID"],
)
def batch_generate(count: int = 5):
    """Generates up to 20 random UUIDs in one call."""
    if count < 1 or count > 20:
        raise HTTPException(status_code=400, detail="count must be between 1 and 20")
    return {"uuids": [str(uuid4()) for _ in range(count)]}
 