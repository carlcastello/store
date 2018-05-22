from flask import Blueprint
from flask_restful import Api
from app.exceptions import ERRORS


ROUTES_BP = Blueprint('api', __name__)

ROUTES = (

)

API = Api(ROUTES_BP, errors=ERRORS)
for route in ROUTES:
    API.add_resource(*route)