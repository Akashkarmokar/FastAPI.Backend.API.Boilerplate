from models.Register import Register as RegisterModel
from core.db import AsyncSession
from sqlalchemy import select
from .helpers import PassHash

class ReadRegisterRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def read_by_id(self,user_id: int) -> None | RegisterModel :
        try:
            async with self.session.begin() as session:
                stmt = select(RegisterModel.id, RegisterModel.email).where(RegisterModel.id == user_id)
                user_details = await session.execute(stmt)
                user_details = user_details.one_or_none()
                return user_details
        except Exception as e:
            print("Error: ", e)
            print('Something went wrong with internal server')
            return None

    async def read_by_email(self, email_address: str) -> None | RegisterModel:
        try:
            async with self.session.begin() as session:
                stmt = select(RegisterModel.id, RegisterModel.email, RegisterModel.password).where(RegisterModel.email == email_address)
                user_details = await session.execute(stmt)
                user_details = user_details.one_or_none()
                return user_details
        except Exception as e :
            print("Error: ", e)
            print("Something went wrong with internal server")
            return None


class CreateRegisterRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self,email: str, plain_password: str):
        try:
            async with self.session.begin() as session:
                hash_pass = PassHash().get_hash_password(plain_password= plain_password)
                user = RegisterModel(email=email, password = hash_pass)
                session.add(user)
                await session.commit()
                created_user = await ReadRegisterRepository(self.session).read_by_id(user.id)
                return created_user
        except Exception as err:
            print('Something went wrong  from repository!!')
            return None