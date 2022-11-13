from flask import Blueprint, jsonify, request, abort
from init import db, bcrypt, jwt
from datetime import timedelta
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from models.users import User, UserSchema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# Route to obtain a list of users and their recipes (admin)
@auth_bp.route("/users/", methods=["GET"])
@jwt_required()
def get_users():
    admin_test()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=["password"]).dump(users), 200

# Route to register a new user
@auth_bp.route("/register/", methods=["POST"])
def register():
    data = UserSchema().load(request.json)
    try:
        user = User(
            username = request.json["username"],
            first_name = request.json["first_name"],
            password = bcrypt.generate_password_hash(request.json["password"]).decode("utf-8")
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=["password"]).dump(user), 201
    except IntegrityError:
        return {"error": "Username has already been registered. Please try a different username."}, 404
    except KeyError:
        return {"error": "Please ensure that a username, first name and password have been provided."}, 400


# Route to login into an existing user and obtain a token
@auth_bp.route("/login/", methods=["POST"])
def auth_login():
    stmt = db.select(User).filter_by(username=request.json["username"])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):

        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=1))
        return {'username': user.username, 'token': token}, 200
    else:
        return {'error': 'Invalid username or password'}, 401


# check an entire user's information (admin)
@auth_bp.route("/users/<username>/", methods=["GET"])
@jwt_required()
def user_info(username):
    admin_test()
    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    return UserSchema(exclude=["password"]).dump(user), 200


# delete a user from the database (admin)
@auth_bp.route("/users/<username>/del/", methods=["DELETE"])
@jwt_required()
def delete_user(username):
    admin_test()
    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"{username} has been deleted"}, 200
    else:
        return {"message": f"{username} does not exist in the database"}, 400



# function to authorise admin actions
def admin_test():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

