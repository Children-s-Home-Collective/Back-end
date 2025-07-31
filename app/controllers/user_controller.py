from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from app import db
from app.models.user import User
from app.schemas.user_schema import user_schema,user_list_schema
from app.utils.constants import TRUSTED_ADMIN_DOMAINS
from marshmallow import ValidationError

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')

        if not all([name, email, password, phone_number]):
            return jsonify({"error": "Missing required fields", "details": "Name, email, password, and phone number are required"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered", "details": f"Email {email} is already in use"}), 400

        role = "admin" if any(email.endswith(domain) for domain in TRUSTED_ADMIN_DOMAINS) else "user"
        user = User(name=name, email=email, phone_number=phone_number, role=role)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        access_token = create_access_token(identity=user.id)
        return jsonify({
            "user": user_schema.dump(user),
            "access_token": access_token,
            "type": "Bearer"
        }), 201

    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user)), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500
    

@user_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_users():
    try:
        users = User.query.all()
        return jsonify(user_list_schema.dump(users)), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500