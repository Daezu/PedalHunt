


import logging
log = logging.getLogger(__name__)

from fastapi.exceptions import HTTPException
from fastapi import Request


defaultMessage = "An unexpected error ocured!"





from fastapi import HTTPException
from pydantic import ValidationError
async def handle_ValidationError(request: Request, error: ValidationError):
    raise HTTPException(status_code=422, detail = error.errors())

from fastapi.exceptions import ResponseValidationError
async def handle_ResponseValidationError(request: Request, error: ResponseValidationError):
    raise HTTPException(status_code=422, detail = error.errors())



# default exception handler
# -> handles every exception, that is not cought seperatly

async def handle_default(request: Request, error: Exception):
    log.exception(error)
    raise HTTPException(400, str(defaultMessage))



class NotFoundException(HTTPException):
    def __init__(self, target: str = "Object", detail: str = " not found!"):
        super().__init__(status_code=400, detail=target + detail)
    

# Security
class AuthenticationException(HTTPException):
    def __init__(self, detail: str = "Authentication failed!"):
        super().__init__(401, detail)

class AuthorizationException(HTTPException):
    def __init__(self, detail: str = "Authorization failed!"):
        super().__init__(403, str(detail))
