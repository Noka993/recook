from app.config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Recipe(db.Model):
    __tablename__ = 'recipe'

    recipe_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.String(120), nullable=False)
    difficulty = db.Column(db.String(120), nullable=False)  # Consider using Enum in the future
    instructions = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    number_of_favorites = db.Column(db.Integer, nullable=False, default=0)

    def to_json(self):
        return {
            'recipeId': str(self.recipe_id),
            'title': self.title,
            'description': self.description,
            'ingredients': [i.strip() for i in self.ingredients.split(',')],
            'difficulty': self.difficulty,
            'instructions': self.instructions,
            'image': self.image,
            'numberOfFavorites': self.number_of_favorites
        }
