from flask import Blueprint, request, jsonify
from app import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from app.models.user import User
from app.utils.constants import TRUSTED_ADMIN_DOMAINS
user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not all([name, email, password]):
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400
    
    role = "admin" if any(email.endswith(domain) for domain in TRUSTED_ADMIN_DOMAINS) else "user"

    hashed_pw = generate_password_hash(password)
    user = User(name=name, email=email, role=role, password=hashed_pw)

    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user.id)

    return jsonify({
        "user":user.serialize(),
        "access_token": access_token,
        "type": "Bearer"
        }), 201


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize())
