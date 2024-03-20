import httpx
import boto3
from core.settings import config
from furl import furl

class AWS_S3:
    def __init__(self):
        self.S3_CLIENT = boto3.client(
            service_name = 's3',
            region_name = config.AWS_REGION_NAME,
            aws_access_key_id = config.AWS_S3_CLIENT_ACCESS_KEY,
            aws_secret_access_key = config.AWS_S3_CLIENT_SECRET_ACCESS_KEY
        )
        self.bucket_name = config.AWS_S3_BUCKET_NAME

    
    async def get_put_object_presigned_url(self, image_key):
        try:
            image_key = image_key or 'bio_image.png'
            presigned_url = self.S3_CLIENT.generate_presigned_url(
                ClientMethod = 'put_object',
                Params = {
                    'Bucket': self.bucket_name,
                    'Key': image_key
                },
                ExpiresIn = 60 * 2
            )
            return {'presigned_url': presigned_url,'image_key': image_key }
            
        except Exception as e:
            print("Error: ", e)
            return ""
        
    async def get_get_object_presigned_url(self, image_key):
        try:
            url = self.S3_CLIENT.generate_presigned_url(
                ClientMethod ='get_object',
                Params = {
                    'Bucket': self.bucket_name,
                    'Key': image_key
                }
            )
            print("URL :" ,url)
            return url
        except Exception as e:
            print("Error :", e)
            return ""
        