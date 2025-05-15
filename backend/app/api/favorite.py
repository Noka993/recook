import uuid
from flask import Blueprint, request
from app.models import FavoriteRecipe
from app.helpers.response_message import response_message
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.config import db

favorites = Blueprint("favorites", __name__)


@favorites.route("/", methods=["GET"])
@jwt_required()
def get_favorites():
    user_id = uuid.UUID(get_jwt_identity())
    favorites = FavoriteRecipe.query.filter_by(user_id=user_id).all()
    return [favorite.to_json() for favorite in favorites], 200


@favorites.route("/", methods=["POST"])
@jwt_required()
def add_favorite():
    data = request.json
    user_id = uuid.UUID(get_jwt_identity())
    favorite_db = FavoriteRecipe.query.filter_by(
        user_id=user_id, recipe_id=data.get("recipeId")
    ).first()

    if favorite_db:
        return response_message("Favorite already exists", 400)

    new_favorite = FavoriteRecipe(**data)
    try:
        db.session.add(new_favorite)
        db.session.commit()
        return new_favorite, 201
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@favorites.route("/", methods=["DELETE"])
@jwt_required()
def delete_favorite():
    data = request.json
    favorite = FavoriteRecipe.query.filter_by(
        user_id=data.get("userId"), recipe_id=data.get("recipeId")
    ).first()

    if not favorite:
        return "Favorite not found", 404
    try:
        db.session.delete(favorite)
        db.session.commit()
        return response_message("Favorite deleted", 204)
    except Exception as e:
        db.session.rollback()
        return str(e), 400
