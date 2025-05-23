from flask import Blueprint, request
from app.models import Ingredients, RecipeIngredient, UserRecipe, Recipe
from app.helpers.response_message import response_message
from app.config import db
from app.helpers.schemas import IngredientOut, IngredientsOut, RecipesOut
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
import uuid

# Define a blueprint for ingredient-related routes
ingredients = Blueprint("ingredients", __name__)


@ingredients.route("/", methods=["POST"])
@jwt_required()
def create_ingredient():
    """
    Create a new ingredient and associate it with a recipe.
    """
    data = request.json
    new_ingredient = Ingredients(name=data.get("name"), category=data.get("category"))
    recipe_id = uuid.UUID(data.get("recipe_id"))
    user_id = uuid.UUID(get_jwt_identity())

    try:
        # Check if the user is authorized to add ingredients to the specified recipe
        recipe = UserRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=user_id
        ).first()
        if not recipe:
            return response_message(
                "You are not authorized to add this ingredient", 403
            )
        # Add the new ingredient to the database
        db.session.add(new_ingredient)
        db.session.commit()
        validated_ingredient = IngredientOut.model_validate(new_ingredient)

        # Create an association between the new ingredient and the recipe
        new_recipe_ingredient = RecipeIngredient(
            recipe_id=recipe_id, ingredient_id=new_ingredient.ingredient_id
        )
        db.session.add(new_recipe_ingredient)
        db.session.commit()
        return validated_ingredient.model_dump_json(), 201

    except IntegrityError:
        return response_message("Ingredient already exists", 400)

    except Exception as e:
        db.session.rollback()
        return str(e), 400


@ingredients.route("/<uuid:ingredient_id>", methods=["DELETE"])
def delete_ingredient(ingredient_id: uuid.UUID):
    """
    Delete an ingredient by its ID.
    """
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
def update_ingredient(ingredient_id: uuid.UUID):
    """
    Update an ingredient's details by its ID.
    """
    data = request.json
    ingredient = Ingredients.query.get(ingredient_id)

    if not ingredient:
        return response_message("Ingredient not found", 404)
    for key, value in data.items():
        setattr(ingredient, key, value)

    try:
        db.session.commit()
        validated_ingredient = IngredientOut.model_validate(ingredient)
        return validated_ingredient.model_dump_json(), 200
    except Exception as e:
        db.session.rollback()
        return str(e), 400


@ingredients.route("/", methods=["GET"])
def get_ingredients():
    """
    Retrieve a list of ingredients with optional search, limit, and offset.
    """
    search = request.args.get("search")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int)

    query = Ingredients.query
    if search:
        query = query.filter(Ingredients.name.ilike(f"%{search}%"))
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    ingredients = query.all()
    validated_ingredients = IngredientsOut.model_validate({"ingredients": ingredients})
    return validated_ingredients.model_dump_json(), 200


@ingredients.route("/<uuid:ingredient_id>", methods=["GET"])
def get_ingredient_by_id(ingredient_id: uuid.UUID):
    """
    Retrieve an ingredient by its ID.
    """
    ingredient = Ingredients.query.get(ingredient_id)
    if not ingredient:
        return response_message("Ingredient not found", 404)
    validated_ingredient = IngredientOut.model_validate(ingredient)
    return validated_ingredient.model_dump_json(), 200


@ingredients.route("/<uuid:ingredient_id>/recipes", methods=["GET"])
def get_ingredient_recipes(ingredient_id: uuid.UUID):
    """
    Retrieve recipes associated with a specific ingredient.
    """
    search = request.args.get("search")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int)

    query = RecipeIngredient.query.join(
        Recipe, Recipe.recipe_id == RecipeIngredient.recipe_id
    ).filter(RecipeIngredient.ingredient_id == ingredient_id)

    if search:
        query = query.filter(Ingredients.name.ilike(f"%{search}%"))
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    recipes = query.all()
    validated_recipes = RecipesOut.model_validate(
        {"recipes": [recipe.recipe for recipe in recipes]}
    )
    return validated_recipes.model_dump_json(), 200


@ingredients.route("/category/<string:category>", methods=["GET"])
def get_ingredient_by_category(category: str):
    """
    Retrieve an ingredient by its category.
    """
    search = request.args.get("search")
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int)

    query = Ingredients.query.filter(Ingredients.category.ilike(category))
    if search:
        query = query.filter(Ingredients.name.ilike(f"%{search}%"))
    if limit:
        query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    ingredients = query.all()
    if not ingredients:
        return response_message("Ingredient not found", 404)
    
    validated_ingredient = IngredientsOut.model_validate({"ingredients": ingredients})
    return validated_ingredient.model_dump_json(), 200


@ingredients.route("/<uuid:ingredient_id>/recipes", methods=["POST"])
def add_ingredient_to_recipe(ingredient_id: uuid.UUID):
    """
    Add an existing ingredient to a specific recipe.
    """
    data = request.json
    recipe_id = uuid.UUID(data.get("recipe_id"))

    try:
        # Check if the ingredient is already added to the recipe
        recipe_ingredient = RecipeIngredient.query.filter_by(
            recipe_id=recipe_id, ingredient_id=ingredient_id
        ).first()
        if recipe_ingredient:
            return response_message("Ingredient already added to recipe", 400)

        # Verify the recipe exists
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return response_message("Recipe not found", 404)

        # Verify user authorization
        user_id = uuid.UUID(get_jwt_identity())
        user_recipe = UserRecipe.query.filter_by(
            user_id=user_id, recipe_id=recipe_id
        ).first()
        if not user_recipe:
            return response_message(
                "You are not authorized to add this ingredient to this recipe", 403
            )

        # Add the ingredient to the recipe
        new_recipe_ingredient = RecipeIngredient(
            recipe_id=recipe_id, ingredient_id=ingredient_id
        )
        db.session.add(new_recipe_ingredient)
        db.session.commit()
        validated_recipe_ingredient = RecipeIngredient.model_validate(
            new_recipe_ingredient
        )
        return validated_recipe_ingredient.model_dump_json(), 201

    except Exception as e:
        db.session.rollback()
        return str(e), 400
