from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from datetime import datetime
from models.visit import Visit
from models.user import User
from models.children_home import ChildrenHome

visit_bp = Blueprint('visit_bp', __name__, url_prefix='/visits')


@visit_bp.route('', methods=['POST'])
@jwt_required()
def create_visit():
    data = request.get_json()
    full_name = data.get('full_name')
    phone_number = data.get('phone_number')
    day_to_visit = data.get('day_to_visit')
    home_id = data.get('home_id')
    number_of_visits = data.get('number_of_visits', 1)

    if not all([full_name, phone_number, day_to_visit, home_id]):
        return jsonify({"error": "Missing required fields"}), 400

    current_user_id = get_jwt_identity()

 
    home = ChildrenHome.query.get(home_id)
    if not home:
        return jsonify({"error": "Children's home not found"}), 404

    try:
        day_to_visit = datetime.strptime(day_to_visit, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    visit = Visit(
        full_name=full_name,
        phone_number=phone_number,
        day_to_visit=day_to_visit,
        number_of_visits=number_of_visits,
        user_id=current_user_id,
        home_id=home_id
    )
    db.session.add(visit)
    db.session.commit()

    return jsonify(visit.serialize()), 201

# ii ni ya admin kuona pekee yake
@visit_bp.route('', methods=['GET'])
@jwt_required()
def get_all_visits():
    visits = Visit.query.all()
    return jsonify([v.serialize() for v in visits]), 200

# pia ii
@visit_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_visits_by_user(user_id):
    visits = Visit.query.filter_by(user_id=user_id).all()
    return jsonify([v.serialize() for v in visits]), 200
