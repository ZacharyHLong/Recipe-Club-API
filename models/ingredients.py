from init import db, ma
from marshmallow import fields


class Ingredient(db.Model):
    __tablename__= "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    ingredient_lists = db.relationship("IngredientList", back_populates="ingredient")

class IngredientSchema(ma.Schema):

    class Meta:
        fields = ("id", "name")


