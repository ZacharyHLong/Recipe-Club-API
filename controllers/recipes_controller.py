from flask import Blueprint, jsonify
from init import db
from models.recipes import Recipe, RecipeSchema

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route("/new/")
def recent():
    stmt = db.select(Recipe).order_by(Recipe.date_created.desc(), Recipe.recipe_name)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)

@recipes_bp.route("/<int:user_id>/")
def author(user_id):
    stmt = db.select(Recipe).filter_by(user_id=user_id)
    recipes = db.session.scalars(stmt).all()
    if recipes:
        return RecipeSchema(many=True).dump(recipes)
    else:
        return{'error': f'No recipes were found that match the user id provided'}