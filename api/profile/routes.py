from fastapi import APIRouter
from .schemas import AddMediaDTO
from core.db import AsyncSession
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from .repository import ProfileRepository

ProfileAPP = APIRouter()

@ProfileAPP.post('/add-profile')
async def add_profile(request_body: AddMediaDTO, session: AsyncSession):
    try:
        created_profile = await ProfileRepository(session=session).add_profile(
                organization_name=request_body.organization_name,
                designation=request_body.designation,
                joining_date=request_body.joining_date, 
                last_working_date = None if request_body.last_working_date == None else request_body.last_working_date
            )
        # profileRepo = ProfileRepository(session=session)
        # payload = jsonable_encoder(request_body,exclude_none=True)
        if created_profile == None:
            return JSONResponse(content=jsonable_encoder({
                'status_code': 400,
                'message':'BAD',
                'data': None
            }))
        else:
            return JSONResponse(content=jsonable_encoder({
                'status_code': 400,
                'message':'OK',
                'data': created_profile
            }))

    except Exception as e :
        print("Error: ", e)
        return JSONResponse(content=jsonable_encoder({
            'status_code': 400,
            'message':' BAD',
            'data': None
        }))