from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, request
from app.models.user import User
from app.helpers.response_message import response_message
from flask import jsonify
from app.config import db


login = Blueprint("login", __name__)
register = Blueprint("register", __name__)

@login.route("/", methods=["POST"])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return response_message("Invalid credentials", 401)

    access_token = create_access_token(identity=user.user_id)
    return jsonify(access_token=access_token)


@register.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    hashed = generate_password_hash(password)
    user = User(username=username, password_hash=hashed)
    db.session.add(user)
    db.session.commit()

    return response_message("User registered successfully", 201)
