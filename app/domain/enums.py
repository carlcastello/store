from enum import Enum


class BaseEnum(Enum):

    def __str__(self):
        return self.name

class EmployeeEnum(BaseEnum):
    MANAGER = 1
    SUPERVISOR = 2
    EMPLOYEE = 3

class UserEnum(BaseEnum):
    OWNER = 1
    EMPLOYEE = 2
    ADMIN = 3

class StoreEnum(BaseEnum):
    RETAIL = 1

class CountryEnum(BaseEnum):
    CAN = 1