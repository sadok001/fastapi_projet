
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse


class UserNotFoundError(HTTPException):
    message = "The user you spcecified does not exist."

    def __init__(self):
        super().__init__(status_code=404, detail=UserNotFoundError.message)

    def __str__(self):
        return UserNotFoundError.message


class UserEmailAlreadyExistsError(HTTPException):
    message = "The e-mail you specified already exists."

    def __init__(self):
        super().__init__(status_code=409, detail=UserEmailAlreadyExistsError.message)

    def __str__(self):
        return UserEmailAlreadyExistsError.message


class InvalideUserCodeError(HTTPException):
    message = "The code you specified has expired or invalid"

    def __init__(self):
        super().__init__(status_code=400, detail=InvalideUserCodeError.message)

    def __str__(self):
        return InvalideUserCodeError.message
