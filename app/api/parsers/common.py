from marshmallow import Schema, post_load
from marshmallow.fields import String, Nested, List

from app.domain.enums import ProvinceEnum, CountryEnum
from app.domain.models.info import Address, ContactInfo


class AddressSchema(Schema):
    address = String(required=True)
    city = String(required=True)
    province = String(required=True)
    country = String(required=True)
    postal_code = String(required=True)

    @post_load
    def to_model(self, data: dict) -> Address:
        return Address(
            address=data.get('address', None),
            city=data.get('city', None),
            province=ProvinceEnum[data.get('province', None)],
            country=CountryEnum[data.get('country', None)],
            postal_code=data.get('postal_code', None)   
        )

class ContactInfoSchema(Schema):
    emails = List(String())
    phone_numbers = List(String())

    @post_load
    def to_model(self, data: dict) -> ContactInfo:
        return ContactInfo(
            emails=data.get('emails', []),
            phone_numbers=data.get('phone_numbers', [])
        )
