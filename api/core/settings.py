import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()



class Config(BaseSettings):
    APP_NAME: str = os.environ.get('APP_NAME', "Protfolio")
    DEBUG: bool = bool(os.environ.get('DEBUG', False))
    ENVIRONMENT_MODE: str = os.environ.get('ENVIRONMENT_MODE', 'local')


class LocalConfig(Config):
    # Database Variable
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('DB_PORT')
    DB_USERNAME: str = os.environ.get('DB_USER')
    DB_PASSWORD: str = os.environ.get('DB_PASSWORD')
    DB_NAME: str = os.environ.get('DB_NAME')
    DB_URL: str = f'postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    JWT_SECRET_KEY: str = os.environ.get('JWT_SECRET_KEY') 
    JWT_ALGORITHM: str = os.environ.get('JWT_ALGORITHM') 
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: str = os.environ.get('JWT_ACCESS_TOKEN_EXPIRE_MINUTES') 
    AWS_S3_CLIENT_ACCESS_KEY: str = os.environ.get('AWS_S3_CLIENT_ACCESS_KEY') 
    AWS_S3_CLIENT_SECRET_ACCESS_KEY: str = os.environ.get('AWS_S3_CLIENT_SECRET_ACCESS_KEY') 
    AWS_REGION_NAME: str = os.environ.get('AWS_REGION_NAME') 
    AWS_S3_BUCKET_NAME: str = os.environ.get('AWS_S3_BUCKET_NAME')
    


def get_config():
    env = os.environ.get('ENVIRONMENT_MODE', 'local')
    config_type = {
        'local': LocalConfig() 
    }
    return config_type[env]


config = get_config()
