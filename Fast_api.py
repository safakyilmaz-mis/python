from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Helloo": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/names/{name}")
def read_name(name: str):
    return {"name": name}  # Eksik olan return ifadesi tamamlandı
