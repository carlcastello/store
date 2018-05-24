from marshmallow import Schema, post_load
from marshmallow.fields import String

from app.domain.enums import CountryEnum
from app.domain.models.common import Address

class CreateAddressSchema(Schema):
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
            province=data.get('province', None),
            country=CountryEnum[data.get('country', None)],
            postal_code=data.get('postal_code', None)   
        )

class UpdateAddressSchema(Schema):
    address = String()
    city = String()
    province = String()
    country = String()
    postal_code = String()

    @post_load
    def to_model(self, data: dict) -> Address:
        return Address(
            address=data.get('address', None),
            city=data.get('city', None),
            province=data.get('province', None),
            country=CountryEnum[data.get('country', None)],
            postal_code=data.get('postal_code', None)   
        )