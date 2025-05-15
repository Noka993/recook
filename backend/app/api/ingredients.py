from flask import Blueprint, request
from app.models import Ingredients
from app.helpers.response_message import response_message
from app.config import db
from flask_jwt_extended import jwt_required
import json

ingredients = Blueprint("ingredients", __name__)


@ingredients.route("/", methods=["POST"])
@jwt_required()
def create_ingredient():
    data = request.json
    new_ingredient = Ingredients(name=data.get("name"), category=data.get("category"))
    try:
        db.session.add(new_ingredient)
        db.session.commit()
        return new_ingredient.to_json(), 201
    except Exception as e:
        db.session.rollback()
        return response_message(str(e), 400)


@ingredients.route("/<uuid:ingredient_id>", methods=["DELETE"])
def delete_ingredient(ingredient_id):
    ingredient = Ingredients.query.get(ingredient_id)
    if not ingredient:
        return response_message("Ingredient not found", 404)
    try:
        db.session.delete(ingredient)
        db.session.commit()
        return response_message("Ingredient deleted", 204)
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@ingredients.route("/<uuid:ingredient_id>", methods=["PUT"])
def update_ingredient(ingredient_id):
    data = request.json
    ingredient = Ingredients.query.get(ingredient_id)
    if not ingredient:
        return response_message("Ingredient not found", 404)
    for key, value in data.items():
        setattr(ingredient, key, value)
    try:
        db.session.commit()
        return response_message("Ingredient updated", 200)
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@ingredients.route("/", methods=["GET"])
def get_all_ingredients():
    ingredients = Ingredients.query.all()
    return json.dumps([ingredient.to_json() for ingredient in ingredients]), 200


@ingredients.route("/<uuid:ingredient_id>", methods=["GET"])
def get_ingredient_by_id(ingredient_id):
    ingredient = Ingredients.query.get(ingredient_id)
    return ingredient.to_json(), 200 if ingredient else response_message(
        "Ingredient not found", 404
    )
