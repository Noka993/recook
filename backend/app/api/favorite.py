import uuid
from flask import Blueprint, request
from app.models import FavoriteRecipe, Recipe
from app.helpers.response_message import response_message
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.config import db
from app.helpers.schemas import FavoriteOut, FavoritesOut

favorites = Blueprint("favorites", __name__)


@favorites.route("/", methods=["GET"])
@jwt_required()
def get_favorites():
    user_id = uuid.UUID(get_jwt_identity())
    favorites = (
        FavoriteRecipe.query.join(Recipe, Recipe.recipe_id == FavoriteRecipe.recipe_id)
        .filter_by(user_id=user_id)
        .all()
    )
    validated_favorites = FavoritesOut.model_validate(
        {"favorites": [favorite.recipe for favorite in favorites]}
    )
    return validated_favorites.model_dump_json(), 200


@favorites.route("/", methods=["POST"])
@jwt_required()
def add_favorite():
    data = request.json
    user_id = uuid.UUID(get_jwt_identity())
    recipe_id = uuid.UUID(data.get("recipe_id"))
    favorite_db = FavoriteRecipe.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()

    if favorite_db:
        return response_message("Favorite already exists", 400)

    new_favorite = FavoriteRecipe(user_id=user_id, recipe_id=recipe_id)
    try:
        db.session.add(new_favorite)
        db.session.commit()
        validated_favorite = FavoriteOut.model_validate(new_favorite)
        return validated_favorite.model_dump_json(), 201
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@favorites.route("/", methods=["DELETE"])
@jwt_required()
def delete_favorite():
    data = request.json
    user_id = uuid.UUID(get_jwt_identity())
    recipe_id = uuid.UUID(data.get("recipe_id"))
    favorite = FavoriteRecipe.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()

    if not favorite:
        return response_message("Favorite not found", 404)
    try:
        db.session.delete(favorite)
        db.session.commit()
        return response_message("Favorite deleted", 204)
    except Exception as e:
        db.session.rollback()
        return str(e), 400
