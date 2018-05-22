from flask import request
from flask_restful import Resource

import re

class ResourceBase(Resource):

    _json = _format_json(request.get_json())

    def _format_json(self, json: dict) -> dict:
        camel_pattern = re.compile(r'([A-Z])')
        return {
            camel_pattern.sub(lambda x: '_' + x.group(1).lower(), key): value 
            for key, value in json
        }

class Store(ResourceBase):
    
    def put(self):
        pass

    def post(self):
        pass

class Employee(ResourceBase):

    def put(self):
        pass

    def post(self):
        pass