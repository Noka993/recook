from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey
import uuid


class UserRecipe(db.Model):
    __tablename__ = "user_recipe"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id", ondelete="CASCADE"), nullable=False)
    recipe_id = Column(
        UUID(as_uuid=True), ForeignKey("recipe.recipe_id", ondelete="CASCADE"), nullable=False
    )

    user = db.relationship(
        "User", backref=db.backref("user_recipe", cascade="all, delete-orphan")
    )
    recipe = db.relationship(
        "Recipe", backref=db.backref("user_recipe", cascade="all, delete-orphan")
    )

    def to_json(self):
        return {"id": self.id, "userId": self.user_id, "recipeId": self.recipe_id}
