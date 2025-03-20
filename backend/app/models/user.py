from app.config import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
import uuid

class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String(120), nullable=False)

    def to_json(self):
        return {
            'userId': self.user_id,
            'username': self.username
        }
