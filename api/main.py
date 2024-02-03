from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/another")
async def another():
    return { "messgae": "Hello another test to check route."}


@app.post("/post-method")
async def post_method():
    return { "message": "Hello post-method"}

handler = Mangum(app=app)