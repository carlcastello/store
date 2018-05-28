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

    