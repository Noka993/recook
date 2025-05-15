from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
import uuid

class Ingredients(db.Model):
    __tablename__ = 'ingredients'

    ingredient_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(120), unique=True, nullable=False)
    category = Column(String(120), nullable=False)

    def to_json(self):
        return {
            "ingredientId": str(self.ingredient_id),
            'name': self.name,
            'category': self.category
        }
