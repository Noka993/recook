from app.models import Recipe
from config import db

class RecipeService:
    
    @staticmethod
    def get_all_recipes():
        recipes = Recipe.query.all()
        return [recipe.to_json() for recipe in recipes]
    
    @staticmethod
    def get_recipe_by_id(recipe_id):
        recipe = Recipe.query.get(recipe_id)
        return recipe.to_json() if recipe else None
    
    @staticmethod
    def create_recipe(data):
        try:
            new_recipe = Recipe(**data)
            db.session.add(new_recipe)
            db.session.commit()
            return "Recipe created successfully", 201
        except Exception as e:
            return str(e), 400

    @staticmethod
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

    @staticmethod
    def update_recipe(recipe_id, data):
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
