from init import db, ma
from marshmallow import fields
from datetime import datetime

class Cookbook(db.Model):
    __tablename__= "cookbooks"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    date_created = db.Column(db.Date) 

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    recipe_list_id = db.Column(db.Integer, db.ForeignKey("recipe_lists.id"), nullable=False)

    user = db.relationship("User", back_populates="cookbooks", cascade="all, delete")
    cookbook_libraires = db.relationship("Cookbook", back_populates="cookbooks")
    recipes_lists = db.relationship("RecipeList", back_populates="cookbook")

class CookbookLibrary(db.Model):
    __tablename__= "cookbook_libraries"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cookbook_id = db.Column(db.Integer, db.ForeignKey("cookbooks.id"), nullable=False)

    user = db.relationship("User", back_populates="cookbook_library")
    cookbooks = db.relationship("Cookbook", back_populates="cookbook_libraries")
    
