from flask import Blueprint, request
from app.services.recipe_service import RecipeService
from app.models import Recipe
from app.helpers.response_message import response_message
from app.config import db
import json

recipes = Blueprint("recipes", __name__)


@recipes.route("/", methods=["GET"])
def get_recipes():
    recipes = Recipe.query.all()
    return [recipe.to_json() for recipe in recipes], 200


@recipes.route("/<uuid:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    print(recipe_id)
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return response_message("Recipe not found", 404)
    return recipe.to_json(), 200


@recipes.route("/", methods=["POST"])
def create_recipe():
    data = request.json
    try:
        new_recipe = Recipe(**data)
        db.session.add(new_recipe)
        db.session.commit()
        return response_message("Recipe created successfully", 201)
    except Exception as e:
        return str(e), 400


@recipes.route("/<uuid:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return "Recipe not found", 404
    try:
        db.session.delete(recipe)
        db.session.commit()
        return "Recipe deleted", 200
    except Exception as e:
        return str(e), 400


@recipes.route("/<uuid:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    data = request.json
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return "Recipe not found", 404
    for key, value in data.items():
        setattr(recipe, key, value)
    try:
        db.session.commit()
        return "Recipe updated", 200
    except Exception as e:
        return str(e), 400
