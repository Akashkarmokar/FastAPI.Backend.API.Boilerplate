from mangum import Mangum
from fastapi import FastAPI
from auth.routes import AuthRoutes
from blogs.routes import Blogs_APP
from profile.routes import ProfileAPP

app = FastAPI()

app.mount('/auth', AuthRoutes, 'Auth App')
app.mount('/blog', Blogs_APP, 'Blog App')
app.mount('/profile', ProfileAPP, 'Profile App')

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/another")
async def another():
    return { "messgae": "Hello another test"}


@app.post("/post-method")
async def post_method():
    return { "message": "Hello post-method"}




handler = Mangum(app=app)