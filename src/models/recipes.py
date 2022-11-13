from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length
from datetime import datetime

class Recipe(db.Model):
    __tablename__= "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String, nullable=False)
    preparation_time = db.Column(db.String)
    cooking_time = db.Column(db.String)
    servings = db.Column(db.Integer)
    process = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


    # deletes recipe list if recipe is deleted (cross-check)!!!
    user = db.relationship("User", back_populates="recipes")
    ingredient_lists = db.relationship("IngredientList", back_populates="recipe", cascade="all, delete")


class RecipeSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["username", "id"])
    ingredient_lists = fields.List(fields.Nested("IngredientListSchema"))

    recipe_name = fields.String(required=True, validate=Length(min=1, error="Reicpe name needs to be at least one character long."))

    class Meta:
        fields = ('id', 'recipe_name', 'preparation_time', 'cooking_time', 'servings', 'process', 'date_created', 'user_id', 'ingredient_lists')
        ordered = True

