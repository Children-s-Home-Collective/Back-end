from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import db
from app.models.volunteer import Volunteer
from app.models.user import User
from app.schemas.volunteer_schema import volunteer_schema
from app.utils.decorators import admin_required

volunteer_bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@volunteer_bp.route('/', methods=['POST'])
@jwt_required()
def create_volunteer():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        current_user_id = get_jwt_identity()
        data.pop('id', None)
        data.pop('user_id', None)

        if not all([data.get('name'), data.get('email'), data.get('phone_number')]):
            return jsonify({"error": "Missing required fields", "details": "name, email, and phone_number are required"}), 400

        if not User.query.get(current_user_id):
            return jsonify({"error": "User not found", "details": f"User ID {current_user_id} does not exist"}), 404

        volunteer = volunteer_schema.load(data, session=db.session)
        volunteer.user_id = current_user_id
        db.session.add(volunteer)
        db.session.commit()
        return jsonify(volunteer_schema.dump(volunteer)), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error", "details": "Email may already exist or required fields missing"}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@volunteer_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_all_volunteers():
    try:
        volunteers = Volunteer.query.all()
        new_volunteers = [
            {
                "id": t.id,
                "phone_number": t.phone_number,
                "email": t.email,
                "description": t.description,
                "name": t.name,
                "user_id": t.user_id
            } for t in volunteers
        ]
        return jsonify(new_volunteers), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@volunteer_bp.route('/<int:volunteer_id>', methods=['GET'])
@jwt_required()
def get_volunteer(volunteer_id):
    try:
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        new_volunteer = {
            "id": volunteer.id,
            "phone_number": volunteer.phone_number,
            "email": volunteer.email,
            "description": volunteer.description,
            "name": volunteer.name,
            "user_id": volunteer.user_id
        }
        return jsonify(new_volunteer), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@volunteer_bp.route('/<int:volunteer_id>', methods=['PUT'])
@jwt_required()
def update_volunteer(volunteer_id):
    try:
        current_user_id = get_jwt_identity()
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        if volunteer.user_id != current_user_id:
            return jsonify({"error": "Unauthorized", "details": "You can only update your own volunteer profile"}), 403

        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        data.pop('id', None)
        volunteer = volunteer_schema.load(data, instance=volunteer, session=db.session, partial=True)
        db.session.commit()
        return jsonify(volunteer_schema.dump(volunteer)), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error", "details": "Email may already exist or required fields missing"}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@volunteer_bp.route('/<int:volunteer_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_volunteer(volunteer_id):
    try:
        current_user_id = get_jwt_identity()
        volunteer = Volunteer.query.get_or_404(volunteer_id)
        if volunteer.user_id != current_user_id:
            return jsonify({"error": "Unauthorized", "details": "You can only delete your own volunteer profile"}), 403

        db.session.delete(volunteer)
        db.session.commit()
        return jsonify({"message": f"Volunteer {volunteer_id} deleted successfully"}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500