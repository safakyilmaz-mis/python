from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Users(BaseModel):
    name: str
    age: int
    YOB: int

@app.get("/")
async def root():
    return {"messagee":"Heello Safak"}

@app.get("/about/{aaa}")
async def about_us(aaa, name: Optional[str] = "User", age: Optional[int] = 0) -> dict:
    return {"message":f"{aaa}, Hello {name}, you are {age} years old"}

@app.post("/users")
async def Create_user(create_user: Users):
    return{
        "name": create_user.name,
        "age": create_user.age,
        "YOB": create_user.YOB
    }
