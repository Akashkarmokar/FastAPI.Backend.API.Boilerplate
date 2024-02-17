from models.Profile import Profile
from core.db import AsyncSession
from sqlalchemy import select
from datetime import date

class ProfileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def read_profile_by_id(self, id: int):
        try :
            async with  self.session.begin() as session:
                stmt = select(Profile.id, Profile.organization_name, Profile.designation, Profile.joining_date, Profile.last_working_date).where(Profile.id == id)
                profile_details = await session.execute(stmt)
                profile_details = profile_details.one_or_none()._asdict()
                return profile_details
        except Exception as e:
            return None
    
    async def add_profile(self, organization_name: str, designation: str, joining_date: date, last_working_date: date = None ):
        try:
            async with self.session.begin() as session: 
                new_profile: Profile = None
                if last_working_date == None :
                    new_profile = Profile(organization_name = organization_name, designation = designation, joining_date = joining_date)
                else :
                    new_profile = Profile(full_name = organization_name, designation = designation, joining_date = joining_date, last_working_date = last_working_date)
                session.add(new_profile)
                await session.commit()
                created_profile = await self.read_profile_by_id(new_profile.id)
                return created_profile

        except Exception as err:
            print("Something went wrong from Profile Repository !!")
            return None