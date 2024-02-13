from pydantic import BaseModel, ConfigDict
from typing import Union, Dict, List


# Right Down ALL Requst Schema Below 
class SignupDTO(BaseModel):
    email: str
    password: str 

class SigninDTO(BaseModel):
    email: str
    password: str


# Right Down All Response Model Below
class BaseResponse(BaseModel):
    message: str 
    status_code: int
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)

class CreatedUserData(BaseModel):
    id: int
    email: str
    alive_status: str

class CreatedUserResponse(BaseResponse):
    data: CreatedUserData | None

