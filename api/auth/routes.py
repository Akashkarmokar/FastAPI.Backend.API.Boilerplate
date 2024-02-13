from fastapi import APIRouter, status, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .schemas import SignupDTO, SigninDTO
from .repository import CreateRegisterRepository, ReadRegisterRepository
from models.Register import Register
from core.db import AsyncSession
from .helpers import PassHash

AuthRoutes = APIRouter(tags=["Auth"],prefix="/auth")

@AuthRoutes.post("/sign-up", status_code = status.HTTP_200_OK)
async def signup_user(request_body: SignupDTO, response: Response, session: AsyncSession):
    
    try:
        doesExistAnyUser = await ReadRegisterRepository(session= session).read_by_email(email_address=request_body.email)
        if doesExistAnyUser :
            return JSONResponse(content = {
                "message": "BAD",
                "status_code": 400,
                "data": None
            })
        created_user = await CreateRegisterRepository(session=session).create_user(request_body.email,request_body.password)
        if created_user is not None:
            response.status_code = status.HTTP_201_CREATED
            data = jsonable_encoder({
                "message": "OK",
                "status_code": 200,
                "data": {
                    "id": created_user[0],
                    "email": created_user[1]
                }
            })
            return JSONResponse(content=data)
            
        else:
            data = jsonable_encoder({
                "message": "BAD",
                "status_code": 400,
                "data": None
            })
            return JSONResponse(content=data)
    except Exception as err:
        data = jsonable_encoder({
                "message": "BAD",
                "status_code": 400,
                "data": None
        })
        return JSONResponse(content=data)
        

@AuthRoutes.post('/sign-in')
async def sign_in_user(request_body: SigninDTO, response: Response, session: AsyncSession):
    try :
        isExistUser = await ReadRegisterRepository(session= session).read_by_email(request_body.email)
        if isExistUser :
            credential = PassHash()
            isPasswordOk = credential.verify_password(request_body.password,isExistUser.password)
            if isPasswordOk:
                access_token = credential.create_access_token(
                    data_to_encode= { 
                        'email': isExistUser.email,
                        'id': isExistUser.id 
                    }
                )
                return JSONResponse(content = {
                    'message': "OK",
                    'status_code': 200,
                    'data': {
                        'access_token': access_token,
                        'token_type': 'bearer'
                    }
                })
            else:
                print('HEre it is !!')
                return JSONResponse(content = {
                    "message": "BAD",
                    "status_code": 400,
                    "data": None
                })
        else:
            return JSONResponse(content= {
                "message": "BAD",
                "status_code": 400,
                "data": None
            })
    except Exception as e :
        data = jsonable_encoder({
            "message": "BAD",
            "status_code": 400,
            "data": None
        })
        return JSONResponse(content=data)