from app.domain.enums import CountryEnum


class ContactInfo:

    def __init__(self, 
                 emails: list,
                 phone_numbers: list):
        self._emails = emails
        self._phone_numbers = phone_numbers

class Address:

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
