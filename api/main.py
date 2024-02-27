from mangum import Mangum
from fastapi import FastAPI
from auth.routes import AuthRoutes
from blogs.routes import Blogs_APP
from profile.routes import ProfileAPP
from fastapi.middleware.cors import CORSMiddleware
from bio.routes import BioAPP

app = FastAPI()

allowed_origin = [ "http://localhost:5173" ]
allowed_methods = [ "*" ]
allowed_headers = [ "*" ]
app.add_middleware(CORSMiddleware,allow_origins = allowed_origin, allow_methods = allowed_methods, allow_headers = allowed_headers)

app.mount('/auth', AuthRoutes, 'Auth App')
app.mount('/blog', Blogs_APP, 'Blog App')
app.mount('/profile', ProfileAPP, 'Profile App')
app.mount('/bio', BioAPP, 'Bio APP')

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