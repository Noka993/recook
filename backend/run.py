from flask import Flask
from app.config import app, db
from app.api.recipe_routes import recipe_bp
from app.api.user_routes import user_bp
from app.api.favorite_routes import favorite_bp

app.register_blueprint(recipe_bp, url_prefix='/recipes')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(favorite_bp, url_prefix='/favorites')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)