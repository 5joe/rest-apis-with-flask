from db import db

# mapping between between a row in db to a python class and therefore a python object--
class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # in postgres this will make it autoincrementing --
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),  unique=False, nullable=False) # the constraint with the foreign key will be enforced by some databases and some wont---
    # ask grab me a store object or store model object that has the store_id. from above.
    store = db.relationship("StoreModel", back_populates="items")