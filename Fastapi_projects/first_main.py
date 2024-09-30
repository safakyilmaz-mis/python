from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {'message: hello Safak'}, 200

@app.get("/about")
async def about():
    return {'message: about page'}, 200

@app.get("/contact")
async def contact():
    return {'message: contact page'}, 200