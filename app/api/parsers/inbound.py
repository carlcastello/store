import uuid 

from marshmallow import Schema, post_load
from marshmallow.fields import String, Nested

from app.api.parsers.common import CreateAddressSchema, UpdateAddressSchema
from app.domain.enums import StoreEnum
from app.domain.models.stores import Store, UpdateStore


class CreateStoreSchema(Schema):
    name = String(required=True)
    phone_number = String(required=True)
    address = Nested(CreateAddressSchema)
    store_type = String(required=True)
    
    @post_load
    def to_model(self, data: dict) -> Store:
        return Store(
            id=uuid.uuid4(),
            name=data.get('name', None),
            store_type=StoreEnum[data.get('store_type', None)],
            phone_number=data.get('phone_number', None),
            address=data.get('address'),
            employees=[]
        )

class UpdateStoreSchema(Schema):
    name = String()
    phone_number = String()
    address = Nested(UpdateAddressSchema)
    store_type = String(required=True)
    
    @post_load
    def to_model(self, data: dict) -> Store:
        return UpdateStore(
            name=data.get('name', None),
            store_type=StoreEnum[data.get('store_type', None)],
            phone_number=data.get('phone_number', None),
            address=data.get('address'),
        )