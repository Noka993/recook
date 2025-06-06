from flask import Blueprint, request
from app.models import Recipe, UserRecipe, Ingredients, RecipeIngredient
from app.helpers.response_message import response_message
from app.helpers.schemas import RecipesOut, RecipeOut, IngredientsOut
from app.config import db
from flask_jwt_extended import jwt_required, get_jwt_identity
import uuid

recipes = Blueprint("recipes", __name__)


@recipes.route("/", methods=["GET"])
def get_recipes():
    recipes = Recipe.query.all()
    validated_recipes = RecipesOut.model_validate({"recipes": recipes})
    return validated_recipes.model_dump_json(), 200


@recipes.route("/<uuid:recipe_id>", methods=["GET"])
def get_recipe(recipe_id: uuid.UUID):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return response_message("Recipe not found", 404)
    validated_recipe = RecipeOut.model_validate(recipe)
    return validated_recipe.model_dump_json(), 200


# TODO: Implement adding ingredients to recipe
@recipes.route("/<uuid:recipe_id>/ingredients", methods=["GET"])
def get_recipe_ingredients(recipe_id: uuid.UUID):
    recipe_ingredients = (
        RecipeIngredient.query.join(
            Ingredients, Ingredients.ingredient_id == RecipeIngredient.ingredient_id
        )
        .filter(RecipeIngredient.recipe_id == recipe_id)
        .all()
    )
    validated_ingredients = IngredientsOut.model_validate({"ingredients": recipe_ingredients})
    return validated_ingredients.model_dump_json(), 200


@recipes.route("/", methods=["POST"])
@jwt_required()
def create_recipe():
    data = request.json
    user_id = uuid.UUID(get_jwt_identity())
    try:
        new_recipe = Recipe(**data)
        db.session.add(new_recipe)
        db.session.commit()

        new_user_recipe = UserRecipe(user_id=user_id, recipe_id=new_recipe.recipe_id)
        db.session.add(new_user_recipe)
        db.session.commit()
        validated_recipe = RecipeOut.model_validate(new_recipe)
        return validated_recipe.model_dump_json(), 201
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@recipes.route("/<uuid:recipe_id>", methods=["DELETE"])
@jwt_required()
def delete_recipe(recipe_id: uuid.UUID):
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return "Recipe not found", 404

    user_id = uuid.UUID(get_jwt_identity())
    user_recipe = UserRecipe.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()
    if not user_recipe:
        return response_message("You are not authorized to delete this recipe", 403)

    try:
        db.session.delete(recipe)
        db.session.commit()
        return response_message("Recipe deleted", 204)
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@recipes.route("/<uuid:recipe_id>", methods=["PUT"])
@jwt_required()
def update_recipe(recipe_id: uuid.UUID):
    data = request.json
    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return "Recipe not found", 404

    user_id = uuid.UUID(get_jwt_identity())
    user_recipe = UserRecipe.query.filter_by(
        user_id=user_id, recipe_id=recipe_id
    ).first()
    if not user_recipe:
        return response_message("You are not authorized to update this recipe", 403)

    for key, value in data.items():
        setattr(recipe, key, value)
    try:
        db.session.commit()
        validated_recipe = RecipeOut.model_validate(recipe)
        return validated_recipe.model_dump_json(), 200
    except Exception as e:
        db.session.rollback()
        return str(e), 400
