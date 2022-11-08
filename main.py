from flask import Flask
from init import db, ma
import os


def create_app():
    app = Flask(__name__)

    app.config['SQALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # look to add config file?

    db = SQLAlchemy(app)

    return app