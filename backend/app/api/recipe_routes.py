from flask import Blueprint, request, jsonify
from app.services.recipe_service import RecipeService
from app.helpers.response_message import response_message

recipe_bp = Blueprint('recipes', __name__)

@recipe_bp.route('/', methods=['GET'])
def get_recipes():
    recipes = RecipeService.get_all_recipes()
    return jsonify({'recipes': recipes}), 200

@recipe_bp.route('/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = RecipeService.get_recipe_by_id(recipe_id)
    if not recipe:
        return response_message('Recipe not found', 404)
    return jsonify({'recipe': recipe}), 200

@recipe_bp.route('/', methods=['POST'])
def create_recipe():
    data = request.json
    result, status = RecipeService.create_recipe(data)
    return response_message(result, status)

@recipe_bp.route('/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    result, status = RecipeService.delete_recipe(recipe_id)
    return response_message(result, status)

@recipe_bp.route('/<int:recipe_id>', methods=['PATCH'])
def update_recipe(recipe_id):
    data = request.json
    result, status = RecipeService.update_recipe(recipe_id, data)
    return response_message(result, status)
