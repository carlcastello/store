from flask_restful import HTTPException

ERRORS = {
    "NoIdException": {
        "message": "Id is required",
        "status": 400
    }
}

class NoIdException(HTTPException):
    code = 400