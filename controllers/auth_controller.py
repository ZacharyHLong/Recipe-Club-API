from flask import Blueprint, jsonify, request, abort
from init import db, bcrypt, jwt
from datetime import timedelta

from models.users import User, UserSchema

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/users/')
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)