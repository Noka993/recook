from flask import request, jsonify
from helpers import response_message
from config import app, db
from models import Recipe, User, Favorite

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
    
    try:
        db.session.add(new_recipe)
        db.session.commit()
    except Exception as e:
        return response_message(str(e))
    
    return response_message("Recipe created successfully", 201)
        
    
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


@app.route('/update_recipe/<int:recipe_id>', methods=['PATCH'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    
    if not recipe:
        return response_message("Recipe not found", 404)
    
    recipe_fields = [
        "recipeId", "title", "description", "ingredients",
        "difficulty", "instructions", "image", "numberOfFavorites"
    ]
        
    data = request.json
    recipe.recipe_id = data.get("recipeId", recipe.recipe_id)
    recipe.title = data.get("title", recipe.title)
    recipe.description = data.get("description", recipe.description)
    recipe.ingredients = data.get("ingredients", recipe.ingredients)
    recipe.difficulty = data.get("difficulty", recipe.difficulty)
    recipe.instructions = data.get("instructions", recipe.instructions)
    recipe.image = data.get("image", recipe.image)
    recipe.number_of_favorites = data.get("numberOfFavorites", recipe.number_of_favorites)
    
    try:
        db.session.commit()
    except Exception as e:
        return response_message(str(e))
    
    return response_message('Recipe updated', 200)


@app.route('/create_user', methods=['POST'])
def create_user():
    required_keys = [
        "recipeId", "title", "description", "ingredients",
        "difficulty", "instructions", "image", "numberOfFavorites"
    ]

    data = request.json 
    
    new_user = User(
        username=data.get("username"),
        password_hash=data.get("passwordHash")
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return response_message(str(e))
    
    return response_message("User created successfully", 201)

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return response_message('User not found', 404)
    
    try:
        db.session.delete(user)
        db.session.commit()    
    except Exception as e:
        return response_message(str(e))
    
    return response_message('User deleted', 200)

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    required_keys = ["userId", "recipeId"]

    data = request.json 

    favorite_data = {key: data.get(key) for key in required_keys}

    missing_fields = [key for key, value in favorite_data.items() if not value]

    if missing_fields:
        return response_message(f"Missing required fields: {', '.join(missing_fields)}", 400)

    new_favorite = Favorite(
        user_id=favorite_data["userId"],
        recipe_id=favorite_data["recipeId"]
    )
    
    favorite_db = Favorite.query.filter_by(user_id=favorite_data["userId"], recipe_id=favorite_data["recipeId"]).first()
    if favorite_db:
        return response_message("Favorite already exists", 400)
    
    try:
        db.session.add(new_favorite)
        db.session.commit()
    except Exception as e:
        return response_message(str(e))
    
    return response_message("Favorite added successfully", 201)
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
