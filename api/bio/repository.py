from models.Bio import Bio as BioModel
from core.db import AsyncSession
from sqlalchemy import select, update


class BioRepository:
    def __init__(self,session: AsyncSession) -> None:
        self.session = session
        
    
    async def find_the_bio(self):
        try:
            async with self.session.begin() as session:
                stmt = select(BioModel.id, BioModel.name, BioModel.note, BioModel.image_key, BioModel.designation)
                stmt_result = await session.execute(stmt)
                stmt_result = stmt_result.one_or_none()
                if stmt_result != None :
                    stmt_result = stmt_result._asdict()
                return stmt_result
        except Exception as e:
            print("Find Exce:", e)
            return None
        

    async def create_bio(self, name = None, note = None, designation = None, image_key = None):
        try:
            async with self.session.begin() as session:
                existedBio = await self.find_the_bio()
                if existedBio == None: # If no record exist yet now, create one
                    new_bio = BioModel(name = name, note = note, designation = designation, image_key = image_key)
                    session.add(new_bio)
                    await session.commit()
                else:  # else edit existed one
                    update_data = {}
                    if name:
                        update_data.update({ 'name': name })
                    if note:
                        update_data.update({ 'note': note})
                    if image_key: 
                        update_data.update({ 'image_key': image_key })
                    if designation:
                        update_data.update({ 'designation': designation })
                    
                    update_stmt = update(BioModel).where(BioModel.id == existedBio.get('id')).values(**update_data)
                    update_stmt = await session.execute(update_stmt)
                    await session.commit()
            
            return await self.find_the_bio()
                    
        except Exception as e:
            return None
        
    async def save_image_key(self, image_key):
        try:
            async with self.session.begin() as session:
                new_bio = BioModel()
                session.add()
        except Exception as e:
            return None