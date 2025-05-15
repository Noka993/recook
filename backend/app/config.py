from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-super-key'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)

jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)