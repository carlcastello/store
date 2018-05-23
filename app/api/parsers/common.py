from marshmallow import Schema
from marshmallow.fields import String


class AddressSchema(Schema):
    address = String(required=True)
    city = String(required=True)
    province = String(required=True)
    country = String(required=True)
    postal_code = String(required=True)