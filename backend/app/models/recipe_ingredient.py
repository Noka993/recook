from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
import uuid


class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredient"

    ri_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ingredient_id = Column(
        UUID(as_uuid=True), ForeignKey("ingredients.ingredient_id", ondelete="CASCADE"), nullable=False
    )
    recipe_id = Column(
        UUID(as_uuid=True), ForeignKey("recipe.recipe_id", ondelete="CASCADE"), nullable=False
    )

    ingredient = db.relationship(
        "Ingredients", backref=db.backref("user_recipe", cascade="all, delete-orphan")
    )
    recipe = db.relationship(
        "Recipe", backref=db.backref("user_recipe", cascade="all, delete-orphan")
    )

    def to_json(self):
        return {
            "id": self.ri_id,
            "ingredientId": self.ingredient_id,
            "recipeId": self.recipe_id,
        }
