from fastapi import FastAPI
from core.db import AsyncSession
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .services import BioService

BioAPP = FastAPI()

@BioAPP.get("/change-profile-image")
async def change_profile_image():
    try:
        await BioService().put_object_presigned_url()
        return JSONResponse(content=jsonable_encoder({
            "message": "OK",
            "status_code": 200,
            "data": None
        }))
    except Exception as e:
        print("Error: ", e)

        return JSONResponse(content=jsonable_encoder({
            "message": "BAD",
            "status_code": 400,
            "data": None
        }))