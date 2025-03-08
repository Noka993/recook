from app.models import User
from config import db

class UserService:
    
    @staticmethod
    def create_user(data):
        new_user = User(
            username=data.get("username"),
            password_hash=data.get("passwordHash")
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return "User created successfully", 201
        except Exception as e:
            return str(e), 400

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return "User not found", 404
        try:
            db.session.delete(user)
            db.session.commit()
            return "User deleted", 200
        except Exception as e:
            return str(e), 400
