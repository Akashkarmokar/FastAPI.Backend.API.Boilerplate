from fastapi import APIRouter
from .schemas import SignupDTO

AuthRoutes = APIRouter(tags=["Auth"],prefix="/auth")

@AuthRoutes.post("/")
async def signup_user():
    