from flask import request
from flask_restful import Resource

from app.exceptions import NoIdException
from app.api.parsers.inbound import CreateStoreSchema, UpdateStoreSchema
from app.domain.service import StoreService

class Store(Resource):

    def __init__(self, service: StoreService):
        self._service = service

    def put(self, id: str) -> dict:
        """
            Updates Store

            :param id:
                None
            :return:
                Newly updated Store
            :raises:
                No Id Exception
        """
        if not id:
            raise NoIdException()
        
        new_store_info = UpdateStoreSchema().load(request.get_json())
        self._service.update_store(id, new_store_info)

    def post(self, id: str = None) -> dict:
        """
            Creates Store

            :param id:
                None
            :return:
                Newly Created Store
        """
        new_store = CreateStoreSchema().load(request.get_json())
        self._service.create_store(new_store)
    
class Employee(Resource):

    def __init__(self, service: StoreService):
        self._service = service

    def put(self, id: str) -> dict:
        """
            Updates Employee's store info

            :param id:
                None
            :return:
                Newly Created Employee
            :raises:
                No Id Exception
        """
        if not id:
            raise NoIdException()
