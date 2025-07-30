from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.schemas.user_schema import user_schema 
from app.utils.auth import get_current_user  
from marshmallow import ValidationError



auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({"error": "Missing required fields", "details": "Email and password are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            return jsonify({"error": "Invalid credentials", "details": "Email or password is incorrect"}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({
            "user": user_schema.dump(user),
            "access_token": access_token,
            "type": "Bearer"
        }), 200
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500
@auth_bp.route('/profile', methods=['GET'])  
@jwt_required()
def get_user_profile(): 
    user = get_current_user()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_schema.dump(user))
