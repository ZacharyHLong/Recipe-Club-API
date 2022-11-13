from flask import Flask
from init import db, ma, bcrypt, jwt
import os

from controllers.cli_controller import db_commands
from controllers.auth_controller import auth_bp
from controllers.recipes_controller import recipes_bp
from controllers.ingredients_controller import ingredients_bp
from controllers.ingredient_lists_controller import ingredient_lists_bp



def create_app():
    app = Flask(__name__)

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')


    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(ingredient_lists_bp)
    app.register_blueprint(db_commands)

    return app