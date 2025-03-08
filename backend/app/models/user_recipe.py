from config import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserRecipe(db.Model):
    __tablename__ = 'user_recipe'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'), nullable=False)
    recipe_id = db.Column(UUID(as_uuid=True), db.ForeignKey('recipe.recipe_id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'recipeId': self.recipe_id
        }
