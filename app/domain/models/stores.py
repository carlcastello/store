from datetime import datetime
from typing import List

from app.domain.enums import EmployeeEnum, StoreEnum
from app.domain.models import Domain
from app.domain.models.info import Address
from app.domain.models.users import User


class Documents(Domain):

    def __init__(self):
        pass


class Employee(Domain):
    
    def __init__(self,
                 id: str,
                 employee_type: EmployeeEnum,
                 user: User,
                 documents: List[Documents],
                 starting_date: datetime,
                 ending_date: datetime):
        self._id = id
        self._employee_type = employee_type
        self._user = user
        self._documents = documents
        self._starting_date = starting_date
        self._ending_date = ending_date


class UpdateEmployee(Domain):
    
    def __init__(self,             
                 employee_type: EmployeeEnum,
                 user: User):
        self._employee_type = employee_type
        self._user = user


class Store(Domain):

    def __init__(self, 
                 id: str, 
                 name: str,
                 store_type: str,
                 phone_number: str, 
                 address: Address,
                 employees: List[Employee],
                 created_date: datetime):
        self._id = id
        self._name = name
        self._addres = address
        self._employees = employees
        self._created_date = created_date

    def get_id(self):
        return self._id

    def get_created_date(self):
        return self._created_date


class UpdateStore(Domain):
    
    def __init__(self,
                 name: str,
                 store_type: StoreEnum,
                 phone_number: str, 
                 address: Address):
        self._name = name
        self._store_type = store_type
        self._phone_number = phone_number
        self._address = address
