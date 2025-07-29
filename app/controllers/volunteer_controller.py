from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.volunteer import Volunteer
from app.schemas.volunteer_schema import volunteer_schema, volunteer_list_schema
from app.utils.decorators import admin_required

volunteer_bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')



@volunteer_bp.route('/', methods=['POST'])
def create_volunteer():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    try:
        volunteer = volunteer_schema.load(data)
        db.session.add(volunteer)
        db.session.commit()
        return volunteer_schema.jsonify(volunteer), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error. Email may already exist or required fields missing."}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@volunteer_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_all_volunteers():
    volunteers = Volunteer.query.all()
    return volunteer_list_schema.jsonify(volunteers), 200



@volunteer_bp.route('/<int:volunteer_id>', methods=['GET'])
def get_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    return volunteer_schema.jsonify(volunteer), 200



@volunteer_bp.route('/<int:volunteer_id>', methods=['PUT'])
@jwt_required()
def update_volunteer(volunteer_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    volunteer = Volunteer.query.get_or_404(volunteer_id)

    try:
        volunteer = volunteer_schema.load(data, instance=volunteer, partial=True)
        db.session.commit()
        return volunteer_schema.jsonify(volunteer), 200
    

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error. Email may already exist or required fields missing."}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@volunteer_bp.route('/<int:volunteer_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)

    try:
        db.session.delete(volunteer)
        db.session.commit()
        return jsonify({"message": f"Volunteer {volunteer_id} deleted successfully."}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
