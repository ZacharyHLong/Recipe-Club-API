from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cookbook_libraries = db.relationship("CookbookLibrary", back_populates="user", cascade="all, delete")
    cookbooks = db.relationship("Cookbook", back_populates="user", cascade="all, delete")
    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    pass