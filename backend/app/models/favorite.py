from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
import uuid


class FavoriteRecipe(db.Model):
    __tablename__ = "favorite_recipe"

    favorite_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id", ondelete="CASCADE"), nullable=False)
    recipe_id = Column(
        UUID(as_uuid=True), ForeignKey("recipe.recipe_id", ondelete="CASCADE"), nullable=False
    )

    user = db.relationship(
        "User", backref=db.backref("favorites", cascade="all, delete-orphan")
    )
    recipe = db.relationship(
        "Recipe",
        backref=db.backref("favorited_by", cascade="all, delete-orphan"),
    )

    def to_json(self):
        return {
            "favorite_id": str(self.favorite_id),
            "user_id": str(self.user_id),
            "recipe_id": str(self.recipe_id),
        }
