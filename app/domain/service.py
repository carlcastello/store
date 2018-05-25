from app.domain.models.stores import Store, UpdateStore, Employee, UpdateEmployee
from app.domain.models.users import User, UpdateUser


class UserService:
    
    def __init__(self):
        pass
    
    def update_user(self, user_id: str, new_user_info: UpdateUser) -> User:
        pass

class StoreService:

    def __init__(self):
        pass

    def create_store(self, new_store: Store) -> Store:
        return None

    def update_store(self, store_id: str, new_store_info: UpdateStore) -> Store:
        return None

    def create_employee(self, store_id: str, new_employee: Employee) -> Employee:
        return None

    def update_employee(self, store_id: str, employee_id: str, new_employee_info: UpdateEmployee) -> Employee:
        return None