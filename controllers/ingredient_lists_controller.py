from flask import Blueprint, jsonify
from init import db
from models.ingredient_list import IngredientList, IngredientListSchema



ingredient_lists_bp = Blueprint('ingredient_lists', __name__, url_prefix='/ingredient_lists')

@ingredient_lists_bp.route("/", methods=["GET"])
def ingredient_list():
    stmt = db.select(IngredientList).order_by(IngredientList.id.asc())
    result = db.session.scalars(stmt)
    return IngredientListSchema(many=True).dump(result), 200
    
    
