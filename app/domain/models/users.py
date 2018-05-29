from datetime import datetime

from app.domain.models import Domain
from app.domain.enums import UserEnum
from app.domain.models.info import Address, ContactInfo


class User(Domain):

    def __init__(self,
                 id: str,
                 first_name: str,
                 last_name: str,
                 username: str,
                 user_type: UserEnum,
                 address: Address,
                 contact_info: ContactInfo,
                 created_date: datetime):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._user_type = user_type
        self._address = address
        self._contact_info = contact_info
        self._created_date = created_date
    
    def get_id(self):
        return self._id
    
    def get_created_date(self):
        return self._created_date


class UpdateUser(Domain):

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 username: str,
                 user_type: UserEnum,
                 address: Address,
                 contact_info: ContactInfo):
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._user_type = user_type
        self._address = address
        self._contact_info = contact_info
