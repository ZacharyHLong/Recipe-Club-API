from flask import Blueprint, jsonify, request
from init import db, ma, jwt
from models.ingredient_list import IngredientList, IngredientListSchema
from flask_jwt_extended import get_jwt_identity, jwt_required



ingredient_lists_bp = Blueprint('ingredient_lists', __name__, url_prefix='/ingredient_lists')

@ingredient_lists_bp.route("/", methods=["GET"])
def ingredient_list():
    stmt = db.select(IngredientList).order_by(IngredientList.id.asc())
    result = db.session.scalars(stmt)
    return IngredientListSchema(many=True).dump(result), 200

@ingredient_lists_bp.route("/", methods=['POST'])
@jwt_required()
def new_recipe():
    try:
        ingredient_list = IngredientList(
            ingredient_id = request.json["ingredient_id"],
            measurement = request.json["measurement"],
            recipe_id = request.json["recipe_id"],
            )
        db.session.add(ingredient_list)
        db.session.commit()
        return(f"Successfully added ingredient to the list")
    except KeyError:
        return {"error": "A recipe id and an ingredient id must be provided."}, 409

        
    
    
