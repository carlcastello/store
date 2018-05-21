from flask import Blueprint
from flask_restful import Api
from app.exceptions import ERRORS


ROOT_BP = Blueprint('api', __name__)
ROOT = Api(ROOT_BP, errors=ERRORS)
