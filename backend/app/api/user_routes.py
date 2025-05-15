from flask import Blueprint, request
from app.models import User
from app.helpers.response_message import response_message
from app.config import db

users = Blueprint("users", __name__)


@users.route("/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return response_message("User not found", 404)
    try:
        db.session.delete(user)
        db.session.commit()
        return 204
    except Exception as e:
        return str(e), 400


@users.route("/<uuid:user_id>", methods=["PUT"])
def update_password(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return response_message("User not found", 404)
    user.password_hash = data.get("passwordHash")
    try:
        db.session.commit()
        return "Password updated", 200
    except Exception as e:
        return str(e), 400