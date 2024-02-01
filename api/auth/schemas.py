from pydantic import BaseModel

class SignupDTO(BaseModel):
    email: str
    password: str 