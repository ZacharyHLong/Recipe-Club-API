from flask import Blueprint
from init import db
from models.ingredients import Ingredient, IngredientSchema

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')


@ingredients_bp.route("/")
def ingredients():
    stmt = db.select(Ingredient)
    ingredients = db.session.scalars(stmt).all()
    return IngredientSchema(many=True).dump(ingredients)