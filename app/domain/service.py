from uuid import uuid4
from datetime import datetime

from app.domain.models.info import ChangeLog
from app.domain.models.stores import Store, UpdateStore, Employee, UpdateEmployee
from app.domain.models.users import User, UpdateUser
from app.infrastructure.repository import UserRepository, ChangeLogRepository, StoreRepository


class UserService:
    
    def __init__(self, user_repository: UserRepository, change_log_repository: ChangeLogRepository):
        self._user_repository = user_repository
        self._change_log_repository = change_log_repository
    
    def update_user(self, user_id: str, new_user_info: UpdateUser) -> User:
        user = self._user_repository.find_by_id(user_id)
        updated_user = User(
            id=user.get_id(),
            created_date=user.get_created_date(),
            **new_user_info.to_dict(is_nested=False)
        )
        if user != updated_user:        
            self._user_repository.save_user(updated_user)
            self._change_log_repository.save_user_change_log(
                ChangeLog(id=user.get_id(), message=ChangeLog.USER_INFO_CHANGED, created_date=datetime.now())
            )
        return updated_user

class StoreService:

    def __init__(self, store_repository: StoreRepository, change_log_repository: ChangeLogRepository):
        self._store_repository = store_repository
        self._change_log_repository = change_log_repository

    def create_store(self, new_store: Store) -> Store:
        created_store = self._store_repository.save_store(new_store)
        self._change_log_repository.save_store_change_log(
            ChangeLog(created_store.get_id(), ChangeLog.STORE_CREATED, new_store.get_created_date())
        )
        return created_store

    def update_store(self, store_id: str, new_store_info: UpdateStore) -> Store:
        return None

    def create_employee(self, store_id: str, new_employee: Employee) -> Employee:
        return None

    def update_employee(self, store_id: str, employee_id: str, new_employee_info: UpdateEmployee) -> Employee:
        return None