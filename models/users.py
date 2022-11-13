from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    first_name = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    recipes = db.relationship("Recipe", back_populates="user", cascade="all, delete")


class UserSchema(ma.Schema):
    recipes = fields.List(fields.Nested('RecipeSchema', only=["recipe_name", "date_created"]))
    class Meta:
        fields = ('id', 'username', 'first_name', 'password', 'is_admin', 'recipes')

    password = ma.String(validate=Length(min=8))