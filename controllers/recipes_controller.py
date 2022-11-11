from flask import Blueprint
from models.recipes import Recipe, RecipeSchema

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/new/')
def recent():
    stmt = db.select(Recipe).order_by(Recipe.date_created.desc(), Recipe.recipe_name)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)