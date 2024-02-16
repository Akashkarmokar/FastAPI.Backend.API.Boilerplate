
from typing import Any
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from common.middlewares import BearerTokenCheckMiddleware

Blogs_APP = FastAPI()

Blogs_APP.add_middleware(BearerTokenCheckMiddleware)


@Blogs_APP.get('/get-blogs')
async def get_blogs():
    return {
        'message': 'Hello world'
    }