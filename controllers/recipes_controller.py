from flask import Blueprint
from models.recipes import Recipe

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/')