from app.domain.enums import EmployeeEnum, StoreEnum
from app.domain.models.common import Address
from app.domain.models.users import User


class Store:

    def __init__(self, 
                 id: str, 
                 name: str,
                 store_type: str,
                 phone_number: str, 
                 address: Address,
                 employees: list):
        self._id = id
        self._name = name
        self._addres = address
        self._employees = employees

class UpdateStore:
    
    def __init__(self,
                 name: str,
                 store_type: StoreEnum,
                 phone_number: str, 
                 address: Address):
        self._name = name
        self._store_type = store_type
        self._phone_number = phone_number
        self._address = address

class Employee:
    
    def __init__(self,
                 id: str,
                 eployee_type: EmployeeEnum,
                 user: User,
                 documents: list):
        self._id = id
        self._type = eployee_type
        self._user = user
        self._documents = documents