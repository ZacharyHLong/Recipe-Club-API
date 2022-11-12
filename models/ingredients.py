from init import db, ma
from marshmallow import fields


class Ingredient(db.Model):
    __tablename__= "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    ingredient_lists = db.relationship("IngredientList", back_populates="ingredients")

class IngredientSchema(ma.Schema):
    
    class Meta:
        fields = ('id', 'name')


class IngredientList(db.Model):
    __tablename__= "ingredient_lists"

    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String)

    #foreign keys
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)

    # back populates
    ingredients = db.relationship("Ingredient", back_populates="ingredient_lists")
    recipe = db.relationship("Recipe", back_populates="ingredient_lists")

class IngredientListSchema:
    recipe = fields.Nested('RecipeSchema')
    class Meta:
        fields = ('id', 'measurement', 'ingredient_id')
