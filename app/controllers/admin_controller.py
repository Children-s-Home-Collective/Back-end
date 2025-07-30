from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.models.user import User
from app import db
from app.schemas.user_schema import user_schema, user_list_schema
from app.utils.constants import ALLOWED_PROMOTION_DOMAINS, TRUSTED_ADMIN_DOMAINS
from app.utils.decorators import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard', methods=['GET'])
@jwt_required()
@admin_required
def get_admin_dashboard_data():
    try:
        total_users = User.query.count()
        total_admins = User.query.filter_by(role='admin').count()
        total_regular_users = User.query.filter_by(role='user').count()
        return jsonify({
            "total_users": total_users,
            "total_admins": total_admins,
            "total_regular_users": total_regular_users
        }), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@admin_bp.route('/admins', methods=['GET'])
@jwt_required()
@admin_required
def get_all_admins():
    try:
        admins = User.query.filter_by(role='admin').all()
        return jsonify(user_list_schema.dump(admins)), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@admin_bp.route('/promote/<int:user_id>', methods=['PATCH'])
@jwt_required()
@admin_required
def promote_user_to_admin(user_id):
    try:
        user = User.query.get_or_404(user_id)
        if user.role == 'admin':
            return jsonify({"error": "No change needed", "details": "User is already admin"}), 400

        email_domain = user.email.split('@')[-1]
        if email_domain in TRUSTED_ADMIN_DOMAINS:
            return jsonify({"error": "Unauthorized domain", "details": f"Users with {email_domain} cannot be promoted after demotion"}), 403
        if email_domain not in ALLOWED_PROMOTION_DOMAINS:
            return jsonify({"error": "Unauthorized domain", "details": f"Email domain {email_domain} not allowed for admin promotion"}), 403

        user.role = 'admin'
        db.session.commit()
        return jsonify({"message": f"User {user.name} promoted to admin", "user": user_schema.dump(user)}), 200
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@admin_bp.route('/demote/<int:user_id>', methods=['PATCH'])
@jwt_required()
@admin_required
def demote_admin_to_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        if user.role == 'user':
            return jsonify({"error": "No change needed", "details": "User is already a regular user"}), 400

        user.role = 'user'
        db.session.commit()
        return jsonify({"message": f"User {user.name} demoted to user", "user": user_schema.dump(user)}), 200
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

