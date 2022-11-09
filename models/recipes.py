from init import db, ma
from marshmallow import fields

class Recipe:
    __tablename__= "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String, nullable=False)
    preparation_time = db.Column(db.String)
    cooking_time = db.Column(db.String)
    process = db.Column(db.Text, nullable=False)
    time_created = db.Column(db.#

    ingredientlist = db.relationship('Ingredient', back_populates='ingredient lists')
    #add FK - user id