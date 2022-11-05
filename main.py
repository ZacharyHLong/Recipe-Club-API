from flask import Flask
from flask_sqalchemy import SQAlchemy
import os


def create_app():
    app = Flask(__name__)

    app.config['SQALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')