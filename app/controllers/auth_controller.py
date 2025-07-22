from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User
from utils.auth import get_current_user  

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({
        "access_token": access_token,
        "user": user.serialize()
    })

@auth_bp.route('/profile', methods=['GET'])  
@jwt_required()
def get_user_profile(): 
    user = get_current_user()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize())
