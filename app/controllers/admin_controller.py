from flask import Blueprint, jsonify, request
from app.models.user import User
from app import db
from app.schemas.user_schema import user_schema, user_list_schema

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/dashboard', methods=['GET'])
def get_admin_dashboard_data():
    total_users = User.query.count()
    total_admins = User.query.filter_by(role='admin').count()
    total_regular_users = User.query.filter_by(role='user').count()

    return jsonify({
        "total_users": total_users,
        "total_admins": total_admins,
        "total_regular_users": total_regular_users
    })


@admin_bp.route('/admins', methods=['GET'])
def get_all_admins():
    admins = User.query.filter_by(role='admin').all()
    return jsonify(user_list_schema.dump(admins))


@admin_bp.route('/promote/<int:user_id>', methods=['POST'])
def promote_user_to_admin(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.role == 'admin':
        return jsonify({"message": "User is already an admin"}), 

    user.role = 'admin'
    db.session.commit()

    return jsonify({"message": f"User {user.first_name} {user.last_name} promoted to admin."})


@admin_bp.route('/demote/<int:user_id>', methods=['POST'])
def demote_admin_to_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.role != 'admin':
        return jsonify({"message": "User is not an admin"}), 400

    user.role = 'user'
    db.session.commit()

    return jsonify({"message": f"User {user.first_name} {user.last_name} demoted to regular user."})
