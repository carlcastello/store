from uuid import uuid4
from datetime import datetime

from marshmallow import Schema, post_load
from marshmallow.fields import String, Nested, Raw, List

from app.domain.enums import StoreEnum, UserEnum, CountryEnum, EmployeeEnum, ProvinceEnum
from app.domain.models.common import Address
from app.domain.models.stores import Store, UpdateStore, Employee, UpdateEmployee
from app.domain.models.users import User, UpdateUser, ContactInfo


class AddressSchema(Schema):
    address = String(required=True)
    city = String(required=True)
    province = String(required=True)
    country = String(required=True)
    postal_code = String(required=True)

    @post_load
    def to_model(self, data: dict) -> Address:
        return Address(
            address=data.get('address', None),
            city=data.get('city', None),
            province=ProvinceEnum[data.get('province', None)],
            country=CountryEnum[data.get('country', None)],
            postal_code=data.get('postal_code', None)   
        )

class ContactInfoSchema(Schema):
    emails = List(String())
    phone_numbers = List(String())

    @post_load
    def to_model(self, data: dict) -> ContactInfo:
        return ContactInfo(
            emails=data.get('emails', []),
            phone_numbers=data.get('phone_numbers', [])
        )

class CreateStoreSchema(Schema):
    name = String(required=True)
    phone_number = String(required=True)
    address = Nested(AddressSchema)
    store_type = String(required=True)
    
    @post_load
    def to_model(self, data: dict) -> Store:
        return Store(
            id=uuid4(),
            name=data.get('name', None),
            store_type=StoreEnum[data.get('store_type', None)],
            phone_number=data.get('phone_number', None),
            address=data.get('address'),
            employees=[]
        )

class UpdateStoreSchema(Schema):
    name = String(required=True)
    phone_number = String(required=True)
    address = Nested(AddressSchema)
    store_type = String(required=True)
    
    @post_load
    def to_model(self, data: dict) -> UpdateStore:
        return UpdateStore(
            name=data.get('name', None),
            store_type=StoreEnum[data.get('store_type', None)],
            phone_number=data.get('phone_number', None),
            address=data.get('address'),
        )

class CreateUserSchema(Schema):
    first_name = String(required=True)
    last_name = String(required=True)
    username = String(required=True)
    user_type = String(required=True)
    address = Nested(AddressSchema)
    contact_info = Nested(ContactInfoSchema)

    @post_load
    def to_model(self, data: dict) -> User:
        return User(
            id=uuid4(),
            first_name=data.get('first_name', None),
            last_name=data.get('last_name', None),
            username=data.get('username', None),
            user_type=UserEnum[data.get('user_type', None)],
            address=data.get('address', None),
            contact_info=data.get('contact_info', None)
        )
        
class UpdateUserSchema(Schema):
    first_name = String(required=True)
    last_name = String(required=True)
    username = String(required=True)
    user_type = String(required=True)
    address = Nested(AddressSchema)
    contact_info = Nested(ContactInfoSchema)

    @post_load
    def to_model(self, data: dict) -> User:
        return UpdateUser(
            first_name=data.get('first_name', None),
            last_name=data.get('last_name', None),
            username=data.get('username', None),
            user_type=UserEnum[data.get('user_type', None)],
            address=data.get('address', None),
            contact_info=data.get('contact_info', None)
        )

class CreateEmployeeSchema(Schema):
    employee_type = String()
    user = Nested(CreateUserSchema)
    
    @post_load
    def to_model(self, data: dict) -> Employee:
        return Employee(
            id=uuid4(),
            employee_type=EmployeeEnum[data.get('employee_type', None)],
            user=data.get('user', None),
            documents=[],
            starting_date=datetime.now(),
            ending_date=None
        )

class UpdateEmployeeSchema(Schema):
    employee_type = String()
    user = Nested(UpdateUserSchema)

    @post_load
    def to_model(self, data: dict) -> UpdateEmployee:
        return UpdateEmployee(
            employee_type=EmployeeEnum[data.get('employee_type', None)],
            user=data.get('user', None)
        )
