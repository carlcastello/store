from flask import request
from flask_restful import Resource

import re

from app.api.parsers.inbound import CreateStoreSchema

class Store(Resource):

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
        print(id)

    def post(self, id: str = None) -> dict:
        """
            Creates Store

            :param id:
                None
            :return:
                Newly Created Store
        """
        new_store = CreateStoreSchema().load(request.get_json())


class Employee(Resource):

    def put(self, id: str) -> dict:
        """
            Updates Employee

            :param id:
                None
            :return:
                Newly Created Employee
            :raises:
                No Id Exception
        """
        print(id)

    def post(self, id: str) -> dict:
        """
            Creates Employee

            :param id:
                None
            :return:
                Newly Created Employee
        """
        print(id)