from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) ##since the id is generate by un on uuid.uudi4().hex
    name = fields.Str(required=True) # Since ite required and must be in the JSON payload --
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)