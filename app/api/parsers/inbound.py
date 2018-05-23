import uuid 

from marshmallow import Schema, post_load
from marshmallow.fields import String, Nested

from app.api.parsers.common import AddressSchema

from app.domain.enums import CountryEnum
from app.domain.models.common import Address
from app.domain.models.stores import Store


class CreateStoreSchema(Schema):
    name = String(required=True)
    address = Nested(AddressSchema)
    
    @post_load
    def to_model(self, data: dict) -> Store:
        return Store(
            id=uuid.uuid4(),
            name=data.get('name', None),
            address=Address(
                address=data.get('address', None),
                city=data.get('city', None),
                province=data.get('province', None),
                country=CountryEnum[data.get('country', None)],
                postal_code=data.get('postal_code', None),
            ),
            employees=[]
        )