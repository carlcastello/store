from flask import Blueprint
from flask_restful import Api

from app.exceptions import ERRORS
from app.api.store_api import Store, Employee

ROUTES_BP = Blueprint('api', __name__)
API = Api(ROUTES_BP, errors=ERRORS)

API.add_resource(Store,
                 "/store/<string:id>")

API.add_resource(Employee,
                 "/employee/<string:id>")