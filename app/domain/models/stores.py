from app.domain.enums import EmployeeEnum
from app.domain.models.common import Address


class Store:
    def __init__(self, 
                 id: str, 
                 name: str, 
                 address: Address,
                 employees: list):
        self._id = id
        self._name = name
        self._addres = address
        self._employees = employees

class Employee:
    def __init__(self,
                 id: str,
                 type: EmployeeEnum):
        self._id = id
        self._type = type