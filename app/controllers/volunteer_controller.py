from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import db
from app.models.volunteer import Volunteer

volunteer_bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')



@volunteer_bp.route('/', methods=['POST'])
def create_volunteer():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    try:
        new_volunteer = Volunteer(
            name=data['name'],
            phone_number=data['phone_number'],
            email=data['email'],
            childrens_home=data['childrens_home'],
            description=data['description'],
            user_id=data['user_id'],
            home_id=data['home_id']
        )
        db.session.add(new_volunteer)
        db.session.commit()
        return jsonify(new_volunteer.serialize()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error. Email may already exist or required fields missing."}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@volunteer_bp.route('/', methods=['GET'])
def get_all_volunteers():
    volunteers = Volunteer.query.all()
    return jsonify([v.serialize() for v in volunteers]), 200



@volunteer_bp.route('/<int:volunteer_id>', methods=['GET'])
def get_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)
    return jsonify(volunteer.serialize()), 200



@volunteer_bp.route('/<int:volunteer_id>', methods=['PUT'])
def update_volunteer(volunteer_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    volunteer = Volunteer.query.get_or_404(volunteer_id)

    try:
        volunteer.name = data.get('name', volunteer.name)
        volunteer.phone_number = data.get('phone_number', volunteer.phone_number)
        volunteer.email = data.get('email', volunteer.email)
        volunteer.childrens_home = data.get('childrens_home', volunteer.childrens_home)
        volunteer.description = data.get('description', volunteer.description)
        volunteer.user_id = data.get('user_id', volunteer.user_id)
        volunteer.home_id = data.get('home_id', volunteer.home_id)

        db.session.commit()
        return jsonify(volunteer.serialize()), 200

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Integrity constraint error. Email may already exist or required fields missing."}), 400

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@volunteer_bp.route('/<int:volunteer_id>', methods=['DELETE'])
def delete_volunteer(volunteer_id):
    volunteer = Volunteer.query.get_or_404(volunteer_id)

    try:
        db.session.delete(volunteer)
        db.session.commit()
        return jsonify({"message": f"Volunteer {volunteer_id} deleted successfully."}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
