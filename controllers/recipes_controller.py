from flask import Blueprint, jsonify, abort, request
from init import db
from datetime import date
from models.recipes import Recipe, RecipeSchema
from models.ingredients import Ingredient
from models.ingredient_list import IngredientList
from controllers.auth_controller import admin_test
from flask_jwt_extended import get_jwt_identity, jwt_required


recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

# view all recipes in the database
@recipes_bp.route("/", methods=['GET'])
def recent():
    stmt = db.select(Recipe).order_by(Recipe.date_created.desc(), Recipe.recipe_name)
    recipes = db.session.scalars(stmt).all()
    return RecipeSchema(many=True).dump(recipes)

# view all recipes created by a user
@recipes_bp.route("/<int:user_id>/", methods=['GET'])
def author(user_id):
    stmt = db.select(Recipe).filter_by(user_id=user_id)
    recipes = db.session.scalars(stmt).all()
    if recipes:
        return RecipeSchema(many=True).dump(recipes)
    else:
        return{'error': f'No recipes were found that match the user id provided'}


# view only a single recipe
@recipes_bp.route("/only/<int:id>/", methods=['GET'])
def single_recipe(id):
    stmt = db.select(Recipe).filter_by(id=id)
    recipe = db.session.scalar(stmt)
    return RecipeSchema().dump(recipe)



# add new recipe to the current user's profile
@recipes_bp.route("/", methods=['POST'])
@jwt_required()
def new_recipe():
    data = RecipeSchema().load(request.json)
    current_user = get_jwt_identity()
    try:
        recipe = Recipe(
            recipe_name = request.json["recipe_name"],
            preparation_time = request.json["preparation_time"],
            cooking_time = request.json["cooking_time"],
            servings = request.json["servings"],
            process = request.json["process"],
            date_created = date.today(),
            user_id = current_user
            )
        db.session.add(recipe)
        db.session.commit()
        return RecipeSchema().dump(recipe), 201
    except KeyError:
        return {"error": "Please ensure that every recipe property has been defined."}, 409


# delete recipe (admin only)
@recipes_bp.route("/only/<int:id>/del/", methods=["DELETE"])
@jwt_required()
def delete_recipe(id):
    admin_test()
    stmt = db.select(Recipe).filter_by(id=id)
    recipe = db.session.scalar(stmt)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return {"message": f"Recipe {id} has been deleted"}, 200
    else:
        return {"message": f"No recipe with the id of {id} exists in the database"}, 404


