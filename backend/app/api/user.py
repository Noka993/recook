from flask import Blueprint, request
from app.models import User, UserRecipe, Recipe
from app.helpers.response_message import response_message
from app.helpers.schemas import RecipesOut, UserOut
from app.config import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
import uuid

user = Blueprint("user", __name__)


@user.route("/list", methods=["GET"])
@jwt_required()
def get_users():
    search = request.args.get("search")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int)
    query = User.query
    if search:
        query = query.filter(User.username.ilike(f"%{search}%"))
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)
    users = query.all()
    return {"users": [user.to_json() for user in users]}, 200


@user.route("/", defaults={"user_id": None}, methods=["DELETE"])
@user.route("/<uuid:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id: uuid.UUID):
    if user_id is None:
        user_id_jwt = uuid.UUID(get_jwt_identity())
        if user_id and user_id_jwt != user_id:
            return response_message("You are not authorized to delete this user", 403)
        user_id = user_id_jwt
    user = User.query.get(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        return response_message("User deleted", 204)
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@user.route("/", defaults={"user_id": None}, methods=["PUT"])
@user.route("/<uuid:user_id>", methods=["PUT"])
@jwt_required()
def update_password(user_id: uuid.UUID):
    if user_id is None:
        user_id_jwt = uuid.UUID(get_jwt_identity())
        print(user_id, user_id_jwt)
        if user_id and user_id_jwt != user_id:
            return response_message(
                "You are not authorized to update this user's password", 403
            )
        user_id = user_id_jwt
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return response_message("User not found", 404)
    if not check_password_hash(user.password_hash, data.get("oldPassword")):
        return response_message("Invalid old password", 400)
    if check_password_hash(user.password_hash, data.get("password")):
        return response_message(
            "New password cannot be the same as the old password", 400
        )
    user.password_hash = generate_password_hash(data.get("password"))
    try:
        db.session.commit()
        return response_message("Password updated", 200)
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@user.route("/recipes", methods=["GET"])
@jwt_required()
def get_user_recipes():
    user_id = uuid.UUID(get_jwt_identity())
    print(user_id)
    user_recipes = (
        UserRecipe.query.join(Recipe, Recipe.recipe_id == UserRecipe.recipe_id)
        .filter(UserRecipe.user_id == user_id)
        .all()
    )
    validated_recipes = RecipesOut.model_validate(
        {"recipes": [recipe.recipe for recipe in user_recipes]}
    )
    return validated_recipes.model_dump_json(), 200
