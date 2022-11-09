from init import db, ma
from marshmallow import fields

class Cookbook:
    __tablename__= "cookbooks"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_created = db.Column(db., nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey(users,id), nullable=False)
    # add FK's user-id and recipe-id

class CookbookLibrary:
    __tablename__= "cookbook libraries"

