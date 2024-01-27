from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from typing import Annotated, AsyncIterator
from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from .settings import config
import ssl

db_user_name = config.DB_USERNAME
db_password = config.DB_PASSWORD
db_host = config.DB_HOST
db_port = config.DB_PORT
db_name = config.DB_NAME

DatabaseURL = f'postgresql+asyncpg://{db_user_name}:{db_password}@{db_host}:{db_port}/{db_name}'

ssl_object = ssl.create_default_context()
ssl_object.check_hostname = False
ssl_object.verify_mode = ssl.CERT_NONE

async_engine = create_async_engine(url=DatabaseURL, echo=True, connect_args={"ssl": ssl_object})
async_session_local = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        yield async_session_local
    except SQLAlchemyError as e:
        print(e)

AsyncSession = Annotated[async_sessionmaker, Depends(get_session)]


