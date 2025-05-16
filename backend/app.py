from app.config import app, db

from app.api import login
from app.api import favorite, recipe, user, ingredients


app.register_blueprint(recipe.recipes, url_prefix='/recipes')
app.register_blueprint(user.user, url_prefix='/user')
app.register_blueprint(favorite.favorites, url_prefix='/favorites')
app.register_blueprint(login.login, url_prefix='/login')
app.register_blueprint(login.register, url_prefix='/register')
app.register_blueprint(ingredients.ingredients, url_prefix='/ingredients')
app.register_blueprint(login.logout, url_prefix='/logout')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
