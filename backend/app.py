from app.config import app, db
from app.api.recipe_routes import recipes
from app.api.user_routes import users
from app.api.favorite_routes import favorites


app.register_blueprint(recipes, url_prefix='/recipes')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(favorites, url_prefix='/favorites')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# TODO: Auth
# TODO: Pydantic scheme validation
# TODO: Error handling, change all functions to return html codes