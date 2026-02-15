from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserOut(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    # ... fetch user data
    user_data = {"id": user_id, "name": "John Doe", "email": "john@example.com"}
    return user_data