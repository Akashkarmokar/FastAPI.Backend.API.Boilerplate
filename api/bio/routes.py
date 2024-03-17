from fastapi import FastAPI, status, APIRouter
from core.db import AsyncSession
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .services import BioService
from globals.S3 import AWS_S3
from .schema import ProfileChange

from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from .services import BioService


# BioAPP = FastAPI()
BioAPP = APIRouter()

@BioAPP.post("/update")
async def change_profile_image(requet_body: ProfileChange, session: AsyncSession):
    try:
        payload = jsonable_encoder(requet_body, exclude_none = True)
        
        action_type = payload.get('action')
        payload.pop('action')
        response_data = None
        if action_type == 'regular':
            response_data = await BioService(session= session).create_or_update_bio(payload)
        elif action_type == 'get_url':
            response_data = await BioService(session= session).put_object_presigned_url(image_key=payload.get('image_key'))
        elif action_type == 'save_key':
            response_data = await BioService(session=session).create_or_update_bio(payload)
        
        # url = await AWS_S3().get_put_object_presigned_url()
        return JSONResponse(content=jsonable_encoder({
            "message": "OK",
            "status_code": 200,
            "data": response_data
        }))
    except Exception as e:
        print("Error: ", e)

        return JSONResponse(content=jsonable_encoder({
            "message": "BAD",
            "status_code": 400,
            "data": None
        }))
    
    
@BioAPP.get('/info')
async def get_bio(session: AsyncSession):
    try:
        bio_info = await BioService(session = session).get_bio_all_info()
        return JSONResponse(content=jsonable_encoder({
            "message": "OK",
            "status_code": 200,
            "data": bio_info
        }))
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({
            "message": "BAD",
            "status_code": 400,
            "data": None
        }))