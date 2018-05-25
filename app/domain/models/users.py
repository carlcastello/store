from app.domain.enums import UserEnum
from app.domain.models.common import Address


class ContactInfo:

    def __init__(self, 
                 emails: list,
                 phone_numbers: list):
        self._emails = emails
        self._phone_numbers = phone_numbers

class User:
    
    def __init__(self,
                 id: str,
                 first_name: str,
                 last_name: str,
                 username: str,
                 user_type: UserEnum,
                 address: Address,
                 contact_info: ContactInfo):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._user_type = user_type
        self._address = address
        self._contact_info = contact_info

class UpdateUser:

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
