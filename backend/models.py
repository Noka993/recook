from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def to_json(self):
        return {
            'user_id': self.id,
            'username': self.username
        }
    
class Recipe(db.Model):
    recipe_id = db.column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.String(120), nullable=False)
    difficulty = db.Column(db.String(120), nullable=False) # Make it an enum in the future
    instructions = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    number_of_favorites = db.Column(db.Integer, nullable=False, default=0)

    def to_json(self):
        return {
            'recipe_id': self.recipe_id,
            'title': self.title,
            'description': self.description,
            'ingredients': [i for i in self.ingredients.split(',')],
            'difficulty': self.difficulty,
            'instructions': self.instructions,
            'image': self.image,
            'number_of_favorites': self.number_of_favorites
        }
    
class UserRecipe(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id
        }
    

class Favorite(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id
        }