from db import db

# mapping between between a row in db to a python class and therefore a python object--
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # in postgres this will make it autoincrementing --
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, unique=False, nullable=False)