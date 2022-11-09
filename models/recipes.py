from init import db, ma
from marshmallow import fields
from datetime import datetime

class Recipe(db.Model):
    __tablename__= "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String, nullable=False)
    preparation_time = db.Column(db.String)
    cooking_time = db.Column(db.String)
    process = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    ingredient_list_id = db.Column(db.Integer, db.ForeignKey("ingredient_lists.id"), nullable=False)

    # deletes recipe list if recipe is deleted (cross-check)!!!
    user = db.relationship("User", back_populates="recipes")
    ingredient_lists = db.relationship("IngredientList", back_populates="recipe", cascade="all, delete")
    recipe_lists = db.relationship("RecipeList", back_populates="recipes")


class RecipeList(db.Model):
    __tablename__ = "recipe_lists"

    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String(50))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)

    recipes = db.relationship("Recipe", back_populates="recipe_list")
    cookbook = db.relationship("Cookbook", back_populates="recipe_lists")
