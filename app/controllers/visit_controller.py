from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from datetime import datetime
from models.visit import Visit
from models.user import User
from models.children_home import ChildrenHome

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
        day_to_visit = datetime.strptime(day_to_visit, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    visitor = visitor(
        full_name=full_name,
        phone_number=phone_number,
        day_to_visit=day_to_visit,
        number_of_visits=number_of_visitors,
        user_id=current_user_id,
        home_id=home_id
    )
    db.session.add(visitor)
    db.session.commit()

    return jsonify(visitor.serialize()), 201


@visitor_bp.route('', methods=['GET'])
@jwt_required()
def get_all_visitors():
    visitors = visitors.query.all()
    return jsonify([v.serialize() for v in visitors]), 200


from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from app import db
from models.visit import Visit
from models.user import User
from models.children_home import ChildrenHome

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
        return jsonify(new_visit.serialize()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# ii n admin tu anaeza ona
@visitor_bp.route('', methods=['GET'])
@jwt_required()
def get_all_visitors():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user or user.role != 'admin':
        return jsonify({"error": "Unauthorized: admin access required"}), 403

    visits = Visit.query.all()
    return jsonify([v.serialize() for v in visits]), 200


# pia ii
@visitor_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_visitors_by_user(user_id):
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    if not user or user.role != 'admin':
        return jsonify({"error": "Unauthorized: admin access required"}), 403

    visits = Visit.query.filter_by(user_id=user_id).all()
    return jsonify([v.serialize() for v in visits]), 200

@visitor_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_visitors_by_user(user_id):
    visitors = visitors.query.filter_by(user_id=user_id).all()
    return jsonify([v.serialize() for v in visitors]), 200
