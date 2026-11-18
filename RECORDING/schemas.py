from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True) ##since the id is generate by un on uuid.uudi4().hex
    name = fields.Str(required=True) # Since ite required and must be in the JSON payload --
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required = True, load_only=True)
    store = fields.Nested(PlainItemSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
