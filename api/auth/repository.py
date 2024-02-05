from models.Register import Register as RegisterModel
from core.db import AsyncSession
from sqlalchemy import select


class ReadRegisterRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def read_by_id(self,user_id: int) -> None | RegisterModel :
        user_details = None
        try:
            async with self.session.begin() as session:
                stmt = select(RegisterModel).where(RegisterModel.id == user_id)
                user_details = await session.scalar(stmt)
                return user_details
        except:
            print('Something went wrong with internal server')
            return None



class CreateRegisterRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self,email: str, hash_password: str) :
        try:
            async with self.session.begin() as session:
                user = RegisterModel(email=email, password = hash_password)
                session.add(user)
                await session.commit()
                created_user = await ReadRegisterRepository(self.session).read_by_id(user.id)
                return created_user
        except Exception as err:
            print('Something went wrong  from repository!!')
            return None