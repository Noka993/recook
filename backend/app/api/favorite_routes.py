from flask import Blueprint, request
from app.services.favorite_service import FavoriteService
from helpers.response_message import response_message

favorite_bp = Blueprint('favorites', __name__)

@favorite_bp.route('/', methods=['POST'])
def add_favorite():
    data = request.json
    result, status = FavoriteService.add_favorite(data)
    return response_message(result, status)
