from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

from app import db
from app.models.visit import Visit
from app.models.user import User
from app.models.children_home import ChildrenHome
from app.schemas.visit_schema import visit_schema, visit_list_schema
from app.utils.decorators import admin_required

visitor_bp = Blueprint('visitor_bp', __name__, url_prefix='/visitor')


@visitor_bp.route('', methods=['POST'])
@jwt_required()
def create_visit():
    data = request.get_json()
    full_name = data.get('full_name')
    phone_number = data.get('phone_number')
    day_to_visit = data.get('day_to_visit')
    home_id = data.get('home_id')
    number_of_visitors = data.get('number_of_visitors', 1)

    if not all([full_name, phone_number, day_to_visit, home_id]):
        return jsonify({"error": "Missing required fields"}), 400

    current_user_id = get_jwt_identity()

    home = ChildrenHome.query.get(home_id)
    if not home:
        return jsonify({"error": "Children's home not found"}), 404

    try:
        visit_date = datetime.strptime(day_to_visit, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    try:
        new_visit = Visit(
            full_name=full_name,
            phone_number=phone_number,
            day_to_visit=visit_date,
            number_of_visits=number_of_visitors,
            user_id=current_user_id,
            home_id=home_id
        )
        db.session.add(new_visit)
        db.session.commit()
        return jsonify(visit_schema.dump(new_visit)), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



@visitor_bp.route('/', methods=['GET'])
# @jwt_required()
# @admin_required
def get_all_visitors():

    visits = Visit.query.all()
    new_visits=[]
    for v in visits:
        n_visit={
            "id":v.id,
            "full_name":v.full_name,
            "phone_number":v.phone_number,
            "day_to_visit":v.day_to_visit,
            "number_of_visitors":v.number_of_visitors,
            "user_id":v.user_id,
            "home_id":v.home_id,
        }
        new_visits.append(n_visit)
    return jsonify(new_visits), 200


@visitor_bp.route('/user/<int:user_id>', methods=['GET'])
# @jwt_required()
# @admin_required
def get_visitors_by_user(user_id):

    visits = Visit.query.filter_by(user_id=user_id).all()
    new_visits=[]
    for b in visits:
        n_visit={
            "id":b.id,
            "full_name":b.full_name,
            "phone_number":b.phone_number,
            "day_to_visit":b.day_to_visit,
            "number_of_visitors":b.number_of_visitors,
            "user_id":b.user_id,
            "home_id":b.home_id,
        }  
        new_visits.append(n_visit)
    return jsonify(new_visits), 200
