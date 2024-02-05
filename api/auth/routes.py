from fastapi import APIRouter, status, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .schemas import SignupDTO, CreatedUserResponse, CreatedUserData
from .repository import CreateRegisterRepository
from models.Register import Register
from core.db import AsyncSession

AuthRoutes = APIRouter(tags=["Auth"],prefix="/auth")

@AuthRoutes.post("/", status_code = status.HTTP_200_OK)
async def signup_user(request_body: SignupDTO, response: Response, session: AsyncSession):
    
    try:
        created_user = await CreateRegisterRepository(session=session).create_user(request_body.email,request_body.password)
        if created_user is not None:
            response.status_code = status.HTTP_201_CREATED
            data = jsonable_encoder({
                "message": "OK",
                "status_code": 200,
                "data":created_user
            })
            return JSONResponse(content=data)
            
        else:
            return CreatedUserResponse(message="BAD", status_code=400, data= CreatedUserData())
    except Exception as err:
        return CreatedUserResponse(message="BAD", status_code=400, data= CreatedUserData())
