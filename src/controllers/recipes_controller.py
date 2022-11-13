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
    return RecipeSchema(many=True).dump(recipes), 200


# view all recipes created by a user
@recipes_bp.route("/<int:user_id>/", methods=['GET'])
def author(user_id):
    stmt = db.select(Recipe).filter_by(user_id=user_id)
    recipes = db.session.scalars(stmt).all()
    if recipes:
        return RecipeSchema(many=True).dump(recipes), 200
    else:
        return{'error': f'No recipes were found that match the user id provided'}, 400


# view only a single recipe
@recipes_bp.route("/<int:user_id>/<int:id>/", methods=['GET'])
def single_recipe(user_id, id):
    stmt = db.select(Recipe).filter_by(id=id)
    recipe = db.session.scalar(stmt)
    return RecipeSchema().dump(recipe), 200



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
        return {"error": "Please ensure that every recipe property has been defined."}, 400


# update a recipe entry (admin only)
@recipes_bp.route('/<int:user_id>/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_recipe(user_id, id):
    admin_test()
    data = RecipeSchema().load(request.json)
    stmt = db.select(Recipe).filter_by(id=id)
    recipe = db.session.scalar(stmt)
    try:
        if recipe:

            recipe.recipe_name = request.json["recipe_name"] or recipe.recipe_name
            recipe.preparation_time = request.json["preparation_time"] or recipe.preparation_time
            recipe.cooking_time = request.json["cooking_time"] or recipe.cooking_time
            recipe.servings = request.json["servings"] or recipe.servings
            recipe.process = request.json["process"] or recipe.process

            db.session.commit()
            return RecipeSchema().dump(recipe)
        else:
            return{'error': f'Recipe not found with an id of {id}'}, 404
    except KeyError:
        return {"error": "Please include each recipe property (even if they are not being changed)."}, 400


# delete recipe (admin only)
@recipes_bp.route("/<int:user_id>/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_recipe(user_id, id):
    admin_test()
    stmt = db.select(Recipe).filter_by(id=id)
    recipe = db.session.scalar(stmt)
    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return {"message": f"Recipe {id} has been deleted"}, 200
    else:
        return {"message": f"No recipe with the id of {id} exists in the database"}, 404


