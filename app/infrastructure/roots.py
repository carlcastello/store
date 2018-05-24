from flask import Blueprint
from flask_restful import Api

from app.domain.service import StoreService
from app.exceptions import ERRORS
from app.api.store_api import Store, Employee

def get_store_service():
    return StoreService()

def get_routes_bp():
    routes_bp = Blueprint('api', __name__)
    api = Api(routes_bp, errors=ERRORS)

    api.add_resource(Store,
                     "/store",                 
                     "/store/<string:id>",
                     resource_class_kwargs={'service': get_store_service()})

    api.add_resource(Employee,
                     "/employee/<string:id>",
                     resource_class_kwargs={'service': get_store_service()})

    return routes_bp
