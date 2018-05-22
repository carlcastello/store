from enum import Enum


class BaseEnum(Enum):

    def __str__(self):
        return self.name

class EmployeeEnum(BaseEnum):
    MANAGER = 1
    SUPERVISOR = 2
    EMPLOYEE = 3
    