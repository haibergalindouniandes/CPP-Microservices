from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendedor = db.Column(db.String(128))
    descripcion = db.Column(db.String(512))
    producto = db.Column(db.Integer)
    cantidad = db.Column(db.Numeric)
    fecha = db.Column(db.Date)


class OrdenSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Orden
        include_relationships = False
        include_fk = False
        load_instance = True

    cantidad = fields.Number()
