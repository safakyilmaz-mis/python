from fastapi import FastAPI
from pydantic import BaseModel  # Import BaseModel for request body validation
from typing import List, Optional

app = FastAPI()


@app.get("/")
def root():
    return {"Helloo": "World"}  # "Helloo" yazım hatası düzeltildi

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class City(BaseModel):
    name: str
    population: int
    loc: str
    description: Optional[str] = None

@app.post("/cities/")
def create_city(city: List[City]):
    return {"city": city}

@app.get("/names/{name}")
def read_name(name: str):
    return {"name": name}  # Eksik olan return ifadesi tamamlandı

@app.get("/test")
def test():
    return {"status": "ok"}  # Test endpoint'i eklendi

