from flask import Blueprint
from flask_restful import Api

from app.domain.service import StoreService, UserService
from app.infrastructure.repository import UserRepository, ChangeLogRepository
from app.exceptions import ERRORS
from app.api.store_api import Store, Employee, User

def get_store_service():
    return StoreService(
        store_repository=None,
        change_log_repository=ChangeLogRepository()
    )

def get_user_service():
    return UserService(
        user_repository=UserRepository(), 
        change_log_repository=ChangeLogRepository()
    )

def get_routes_bp():
    routes_bp = Blueprint('api', __name__)
    api = Api(routes_bp, errors=ERRORS)

    api.add_resource(Store,
                     "/store",                 
                     "/store/<string:store_id>",
                     resource_class_kwargs={'service': get_store_service()})

    api.add_resource(Employee,
                     "/store/<string:store_id>/employee",
                     "/store/<string:store_id>/employee/<string:employee_id>",
                     resource_class_kwargs={'service': get_store_service()})

    api.add_resource(User,
                     "/user/<string:user_id>",
                     resource_class_kwargs={'service': get_user_service()})

    return routes_bp
