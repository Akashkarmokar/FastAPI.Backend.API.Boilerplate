import sys
sys.path.append("...")

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
from typing import Any 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from auth.helpers import PassHash


        
class BearerTokenCheckMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Any) -> Response:
        get_token = request.headers.get('Authorization')
        jwt_token = get_token.split(" ")[1]
        isVerified = PassHash().check_acces_token(jwt_token)
        if isVerified == False:
            return JSONResponse(content=jsonable_encoder({
                "message": "BAD",
                "status_code": 401,
                "data": None
            }))
        response = await call_next(request)
        return response