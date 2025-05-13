from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
import uuid

class UserRecipe(db.Model):
    __tablename__ = 'user_recipe'

    ri_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ingredient_id = Column(UUID(as_uuid=True), ForeignKey('ingredient.ingredient_id'), nullable=False)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey('recipe.recipe_id'), nullable=False)

    def to_json(self):
        return {
            'id': self.ri_id,
            'ingredientId': self.ingredient_id,
            'recipeId': self.recipe_id
        }
