from flask import request
from flask_restful import Resource

import re

class ResourceBase(Resource):
    
    def _get_json(self) -> dict:
        json = request.get_json()
        camel_pattern = re.compile(r'([A-Z])')
        return {
            camel_pattern.sub(lambda x: '_' + x.group(1).lower(), key): value 
            for key, value in json
        }

class Store(ResourceBase):

    def put(self, id):
        print(id)

    def post(self, id):
        print(id)

class Employee(ResourceBase):

    def put(self, id):
        pass

    def post(self, id):
        pass