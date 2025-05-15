from flask import Blueprint, request
from app.models import Favorite
from app.helpers.response_message import response_message
from app.config import db

favorites = Blueprint("favorites", __name__)


@favorites.route("/", methods=["POST"])
def add_favorite():
    data = request.json
    favorite_db = Favorite.query.filter_by(
        user_id=data.get("userId"), recipe_id=data.get("recipeId")
    ).first()

    if favorite_db:
        return "Favorite already exists", 400

    new_favorite = Favorite(**data)
    try:
        db.session.add(new_favorite)
        db.session.commit()
        return new_favorite, 201, True
    except Exception as e:
        return str(e), 400


@favorites.route("/", methods=["DELETE"])
def delete_favorite():
    data = request.json
    favorite = Favorite.query.filter_by(
        user_id=data.get("userId"), recipe_id=data.get("recipeId")
    ).first()
    if not favorite:
        return "Favorite not found", 404
    try:
        db.session.delete(favorite)
        db.session.commit()
        return "Favorite deleted", 200
    except Exception as e:
        return str(e), 400
