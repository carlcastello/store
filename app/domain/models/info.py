from app.domain.models import Domain
from app.domain.enums import CountryEnum


class ContactInfo(Domain):

    def __init__(self, 
                 emails: list,
                 phone_numbers: list):
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

    USER_INFO_CHANGED = "User info has changed"

    def __init__(self,
                 id: str,
                 message: str):
        self._id = id
        self._massage = message