from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


class Ingredient(db.Model):
    __tablename__= "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    ingredient_lists = db.relationship("IngredientList", back_populates="ingredient")

class IngredientSchema(ma.Schema):
    name = fields.String(required=True, validate=Length(min=2, error="Ingredeient name must be at least 2 characters"))
    
    class Meta:
        fields = ("name", "id")



