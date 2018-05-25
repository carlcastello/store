from flask import request
from flask_restful import Resource

from app.exceptions import NoIdException
from app.api.parsers.inbound import CreateStoreSchema, UpdateStoreSchema, CreateEmployeeSchema, UpdateEmployeeSchema
    
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
        updated_store = self._service.update_store(id, new_store_info)
        return updated_store

    def post(self, id: str = None) -> dict:
        """
            Creates Store

            :param id:
                None
            :return:
                Newly Created Store
        """
        new_store = CreateStoreSchema().load(request.get_json())
        creted_store = self._service.create_store(new_store)
        return creted_store

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

        new_employee_info = UpdateEmployeeSchema().load(request.get_json())
        updated_employee = self._service.update_employee(new_employee_info)
        return updated_employee

    def post(self, id: str = None) -> dict:
        """
            Creates new store Employee and User

            :param id:
                None
            :return:
                Newly Created Employee
            :raises:
                No Id Exception
        """
        new_employee = CreateEmployeeSchema().load(request.get_json())
        created_employee = self._service.create_employee(new_employee)
        return created_employee