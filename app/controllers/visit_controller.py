from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from marshmallow import ValidationError
from app import db
from app.models.visit import Visit
from app.models.user import User
from app.models.children_home import ChildrenHome
from app.schemas.visit_schema import visit_schema, visit_list_schema
from app.utils.decorators import admin_required

visitor_bp = Blueprint('visitor_bp', __name__, url_prefix='/visitor')

@visitor_bp.route('/', methods=['POST'])
@jwt_required()
def create_visit():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        # Validate and deserialize input data to dict
        validated_data = visit_schema.load(data, session=db.session)

        # Validate user existence
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if not user:
            return jsonify({"error": "User not found", "details": f"User ID {current_user_id} does not exist"}), 404

        # Validate children home existence
        home = ChildrenHome.query.get(validated_data['home_id'])
        if not home:
            return jsonify({"error": "Children's home not found", "details": f"Home ID {validated_data['home_id']} does not exist"}), 404

        # Validate day_to_visit format
        try:
            visit_date = datetime.strptime(validated_data['day_to_visit'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Invalid date format", "details": "Use YYYY-MM-DD for day_to_visit"}), 400

        # Create Visit model instance
        new_visit = Visit(
            full_name=validated_data['full_name'],
            phone_number=validated_data['phone_number'],
            day_to_visit=visit_date,
            number_of_visitors=validated_data.get('number_of_visitors', 1),
            user_id=current_user_id,
            home_id=validated_data['home_id']
        )

        db.session.add(new_visit)
        db.session.commit()

        # Return the newly created visit serialized
        return jsonify(visit_schema.dump(new_visit)), 201

    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@visitor_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_all_visitors():
    try:
        visits = Visit.query.all()
        new_visits = [
            {
                "id": v.id,
                "full_name": v.full_name,
                "phone_number": v.phone_number,
                "day_to_visit": v.day_to_visit.isoformat(),
                "number_of_visitors": v.number_of_visitors,
                "user_id": v.user_id,
                "home_id": v.home_id
            } for v in visits
        ]
        return jsonify(new_visits), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@visitor_bp.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_visitors_by_user(user_id):
    try:
        if not User.query.get(user_id):
            return jsonify({"error": "User not found", "details": f"User ID {user_id} does not exist"}), 404

        visits = Visit.query.filter_by(user_id=user_id).all()
        new_visits = [
            {
                "id": v.id,
                "full_name": v.full_name,
                "phone_number": v.phone_number,
                "day_to_visit": v.day_to_visit.isoformat(),
                "number_of_visitors": v.number_of_visitors,
                "user_id": v.user_id,
                "home_id": v.home_id
            } for v in visits
        ]
        return jsonify(new_visits), 200
    except SQLAlchemyError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500