from api.models.Register import Register
from api.core.db import AsyncSession


class RegisterRepository:
    def __init__(self,session: AsyncSession) -> None:
        self.assync_session = session
    

    @staticmethod
    def create_hashpassword(original_password: str) -> str:
        return ""

    @staticmethod
    def checkpassword(original_password: str, hash_password: str) -> bool :
        return True

        
    async def create_user(self, email: str, hashed_password: str): 
        async with self.assync_session.begin() as session:

        