from fastapi.exceptions import RequestValidationError
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

async def validation_exception_error(request: Request, exec: RequestValidationError):
    return JSONResponse(
        status_code= status.HTTP_200_OK,
        content= jsonable_encoder({
            "message": "BAD",
            "status_code" : status.HTTP_400_BAD_REQUEST,
            "data": {
                "error_details": exec.errors(),
                "body": exec.body()
            }
        })
    )