from flask import Blueprint, jsonify, request, abort
from init import db, ma, jwt
from sqlalchemy.exc import IntegrityError
from models.ingredients import Ingredient, IngredientSchema
from flask_jwt_extended import get_jwt_identity, jwt_required

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

# a list of all ingredients and their associated id
@ingredients_bp.route("/")
def ingredients():
    stmt = db.select(Ingredient)
    ingredients = db.session.scalars(stmt).all()
    return IngredientSchema(many=True).dump(ingredients), 200

# add new ingredient to the database requires authentication to add an ingredient
@ingredients_bp.route("/", methods=["POST"])
@jwt_required()
def new_ingredients():
    data = IngredientSchema().load(request.json)
    try:
        ingredient = Ingredient(
            name = request.json["name"],
            )
        db.session.add(ingredient)
        db.session.commit()
        return IngredientSchema().dump(ingredient), 201
    except IntegrityError:
        return {"error": "That ingredient is already in the database"}, 400