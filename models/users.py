from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, Regexp, And

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    first_name = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    recipes = fields.List(fields.Nested('RecipeSchema', only=["recipe_name", "date_created"]))
    
    username = fields.String(required=True, validate = And(Length(min=8, max=20, error="Username must be between 8-20 characters"), Regexp("^[a-zA-Z0-9]*$", error = "Username only accepts alphanumeric characters.")))
    first_name = fields.String(required=True, validate = Regexp("^[a-zA-Z]*$", error = "Your first name must only include alphabetical characters."))
    password = fields.String(required=True, validate = Length(min=8, error = "Password must be at least 8 characters"))
    
    class Meta:
        fields = ('id', 'username', 'first_name', 'password', 'is_admin', 'recipes')

    password = ma.String(validate=Length(min=8))