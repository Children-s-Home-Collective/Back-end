from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app.utils.auth import get_current_user  
from app import db



auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email').lower().strip()
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({
        "access_token": access_token,
        "token_type": "Bearer",
        "user": user.serialize()
    }), 200 

@auth_bp.route('/verify-admin', methods=["POST"])
@jwt_required()
def verify_admin():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    data = request.get_json()
    code = data.get("code")

    if code == "ADMIN123":
        user.role = "admin"
        db.session.commit()
        return jsonify({"message": "Admin access granted."}), 200

    return jsonify({"error": "Invalid verification code."}), 403
@auth_bp.route('/profile', methods=['GET'])  
@jwt_required()
def get_user_profile(): 
    user = get_current_user()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize())
