from init import db, ma
from marshmallow import fields

class Ingredient:
    __tablename__= "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Measurement:
    __tablename__= "measurements"

    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String(50))


class IngredientList:
    __tablename__= "ingredient lists"

    id = db.Column(db.Integer, primary_key=True)
    measurement_id = db.Column(db.Integer, db.ForeignKey("measurement.id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)

    measurement = db.relationship('Measurement', back_populates='ingredient lists')
    ingredient = db.relationship('Ingredient', back_populates='ingredient lists')