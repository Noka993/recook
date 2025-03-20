from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Integer
import uuid

class Recipe(db.Model):
    __tablename__ = 'recipe'

    recipe_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(80), nullable=False)
    description = Column(String(120), nullable=False)
    ingredients = Column(String(120), nullable=False)
    difficulty = Column(String(120), nullable=False)  # Consider using Enum in the future
    instructions = Column(String(300), nullable=False)
    image = Column(String(120), nullable=False)
    number_of_favorites = Column(Integer, nullable=False, default=0)

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
