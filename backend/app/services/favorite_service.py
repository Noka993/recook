from app.models import Favorite
from app.config import db

class FavoriteService:
    
    @staticmethod
    def add_favorite(data):
        favorite_db = Favorite.query.filter_by(
            user_id=data.get("userId"), 
            recipe_id=data.get("recipeId")
        ).first()

        if favorite_db:
            return "Favorite already exists", 400
        
        new_favorite = Favorite(**data)
        try:
            db.session.add(new_favorite)
            db.session.commit()
            return "Favorite added successfully", 201
        except Exception as e:
            return str(e), 400
