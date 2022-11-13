from init import db, ma
from marshmallow import fields
from models.ingredients import Ingredient

class IngredientList(db.Model):
    __tablename__ = "ingredient_lists"

    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String)

    #foreign keys
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)

    # back populates
    ingredient = db.relationship("Ingredient", back_populates="ingredient_lists")
    recipe = db.relationship("Recipe", back_populates="ingredient_lists")

class IngredientListSchema(ma.Schema):
    recipe = fields.Nested("RecipeSchema", only=["recipe_name"])
    ingredient = fields.Nested("IngredientSchema", only=["name"])
    
    class Meta:
        fields = ("id", "measurement", "ingredient", "recipe")
        ordered = True
