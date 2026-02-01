from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def generic_exception_handler(request: Request, exc: Exception):
    status_code = 500
    detail = str(exc)

    if isinstance(exc, HTTPException):
        status_code = exc.status_code
        detail = exc.detail

    elif isinstance(exc, RequestValidationError):
        status_code = 422
        detail = exc.errors()

    elif hasattr(exc, 'status_code') and hasattr(exc, 'detail'):
        status_code = exc.status_code
        detail = exc.detail

    return JSONResponse(
        status_code=status_code,
        content={
            'status_code': status_code,
            'detail': detail,
        },
    )
