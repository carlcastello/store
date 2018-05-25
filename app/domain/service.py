from app.domain.models.stores import Store, UpdateStore, Employee, UpdateEmployee

class StoreService:

    def __init__(self):
        pass

    def create_store(self, new_store: Store) -> Store:
        return None

    def update_store(self, new_store_info: UpdateStore) -> Store:
        return None

    def update_employee(self, new_employee_info: UpdateEmployee) -> Employee:
        return None
    
    def create_employee(self, new_employee: Employee) -> Employee:
        return None