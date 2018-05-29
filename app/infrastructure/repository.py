from app.domain.models.stores import Store
from app.domain.models.users import User
from app.domain.models.info import ChangeLog

class UserRepository:
    
    def __init__(self):
        pass

    def find_by_id(self, user_id: str) -> User:
        return None
    
    def save_user(self, user: User) -> User:
        return None

class ChangeLogRepository:

    def __init__(self):
        pass

    def save_user_change_log(self, change_log: ChangeLog) -> ChangeLog:
        return None

    def save_store_change_log(self, change_log: ChangeLog) -> ChangeLog:
        return None

class StoreRepository:

    def __init__(self):
        pass
    
    def save_store(self, store: Store) -> Store:
        return None
    