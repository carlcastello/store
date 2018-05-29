from typing import List

from datetime import datetime
from app.domain.models import Domain
from app.domain.enums import CountryEnum


class ContactInfo(Domain):

    def __init__(self, 
                 emails: List[str],
                 phone_numbers: List[str]):
        self._emails = emails
        self._phone_numbers = phone_numbers


class Address(Domain):

    def __init__(self,
                 address: str,
                 city: str,
                 province: str,
                 country: CountryEnum,
                 postal_code: str):
        self._address = address
        self._city = city
        self._province = province
        self._country = country
        self._postal_code = postal_code

class ChangeLog(Domain):

    STORE_CREATED = 'Store Created'
    USER_INFO_CHANGED = 'User info has changed'

    def __init__(self,
                 id: str,
                 message: str,
                 created_date: datetime):
        self._id = id
        self._massage = message
        self._created_date = created_date