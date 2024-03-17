import httpx
import boto3
from core.settings import config
from globals.S3 import AWS_S3
from core.db import AsyncSession
from .repository import BioRepository

class BioService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def put_object_presigned_url(self, image_key: str):
        try:
            image_url_data = await AWS_S3().get_put_object_presigned_url(image_key=image_key)
            return image_url_data
        except :
            return None
    
    async def create_or_update_bio(self, payload):
        try:
            value  = await BioRepository(self.session).create_bio(**payload)
            return value
        except Exception as e: 
            print("Error : ", e)
            return None
        
    async def get_bio_all_info(self):
        try:
            value = await BioRepository(self.session).find_the_bio()
            print("Value: ", value)
            image_key = await AWS_S3().get_get_object_presigned_url(image_key=value.get('image_key'))
            value.update({'image_key': image_key})
            return value
        except Exception as e:
            return None