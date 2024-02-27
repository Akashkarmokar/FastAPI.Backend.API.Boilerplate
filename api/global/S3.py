import httpx
import boto3
from core.settings import config

class AWS_S3:
    def __init__(self):
        self.AWS_S3_CLIENT_ACCESS_KEY = config.AWS_S3_CLIENT_ACCESS_KEY
        self.AWS_S3_CLIENT_SECRET_ACCESS_KEY = config.AWS_S3_CLIENT_SECRET_ACCESS_KEY