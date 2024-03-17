from mangum import Mangum
from fastapi import FastAPI, status, HTTPException, Request
from auth.routes import AuthRoutes
from blogs.routes import Blogs_APP
from profile.routes import ProfileAPP
from fastapi.middleware.cors import CORSMiddleware
from bio.routes import BioAPP
from fastapi.exceptions import RequestValidationError
# from common.exception_handler import validation_exception_error
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

allowed_origin = [ "http://localhost:5173" ]
allowed_methods = [ "*" ]
allowed_headers = [ "*" ]
app.add_middleware(CORSMiddleware,allow_origins = allowed_origin, allow_methods = allowed_methods, allow_headers = allowed_headers)


@app.exception_handler(RequestValidationError)
async def validation_exception_error(request: Request, exec: RequestValidationError):
    
    return JSONResponse(
        status_code= status.HTTP_400_BAD_REQUEST,
        content = jsonable_encoder({
            "message": "BAD",
            "status_code" : status.HTTP_400_BAD_REQUEST,
            "data": {
                "error_details": exec.errors(),
                "body": exec.body
            }
        })
    )


app.include_router(AuthRoutes, prefix='/auth', tags=['Auth API'])
app.include_router(Blogs_APP, prefix='/blog', tags=['Blogs API'])
app.include_router(ProfileAPP, prefix='/profile', tags=['Profile API'])
app.include_router(BioAPP, prefix="/bio", tags=["Bio API"])

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