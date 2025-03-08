from flask import Blueprint, request
from app.services.user_service import UserService
from app.helpers.response_message import response_message

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    result, status = UserService.create_user(data)
    return response_message(result, status)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result, status = UserService.delete_user(user_id)
    return response_message(result, status)
