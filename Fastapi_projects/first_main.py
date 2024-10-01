from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"messagee":"Heello Safak"}

@app.get("/about/{aaa}")
async def about_us(aaa, name: Optional[str] = "User", age: Optional[int] = 0) -> dict:
    return {"message":f"{aaa}, Hello {name}, you are {age} years old"}

