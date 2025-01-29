from flask import request, jsonify
from helpers import response_message
from config import app, db
from models import Recipe

@app.route('/recipes', method=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    json_recipes = [recipe.to_json() for recipe in recipes]

    return jsonify({
        'recipes': json_recipes
    }), 200

@app.route('/get_recipe', methods=['GET'])
def get_recipe():
    recipe_id = request.args.get('recipe_id', type=int)
    if not recipe_id:
        return response_message('Recipe id not provided', 400)

    recipe = Recipe.query.get(recipe_id)
    if not recipe:
        return response_message('Recipe not found', 404)
    
    return jsonify({
        'recipe': recipe
    }), 200

@app.route('/create_recipe', methods=['POST'])
def create_recipe():
    required_keys = [
        "recipeId", "title", "description", "ingredients",
        "difficulty", "instructions", "image", "numberOfFavorites"
    ]

    data = request.json 

    recipe_data = {key: data.get(key) for key in required_keys}

    missing_fields = [key for key, value in recipe_data.items() if not value]

    if missing_fields:
        return response_message(f"Missing required fields: {', '.join(missing_fields)}", 400)

    new_recipe = Recipe(
        recipe_id=recipe_data["recipeId"],
        title=recipe_data["title"],
        description=recipe_data["description"],
        ingredients=recipe_data["ingredients"],
        difficulty=recipe_data["difficulty"],
        instructions=recipe_data["instructions"],
        image=recipe_data["image"],
        number_of_favorites=recipe_data["numberOfFavorites"]
    )


@app.route('/delete_recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return response_message('Recipe not found', 404)
    
    try:
        db.session.delete(recipe)
        db.session.commit()
    except Exception as e:
        return response_message(str(e))
    
    return response_message('Recipe deleted', 200)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
