from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
import redis

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-super-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]

jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)

redis_blocklist = redis.StrictRedis(
    host="localhost", port=6379, db=0, decode_responses=True
)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return redis_blocklist.get(jti) is not None
