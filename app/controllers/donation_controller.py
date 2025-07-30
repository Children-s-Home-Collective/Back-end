from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.donation import Donation
from app.schemas.donation_schema import donation_schema
from app.utils.decorators import admin_required
from sqlalchemy import func
from marshmallow import ValidationError

donation_bp = Blueprint('donation_bp', __name__, url_prefix="/donations")

@donation_bp.route('/', methods=['POST'])
@jwt_required()
def create_donation():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        current_user_id = get_jwt_identity()
        data['user_id'] = current_user_id
        data.pop('id', None)

        if not all([data.get('amount'), data.get('donation_type'), data.get('home_id')]):
            return jsonify({"error": "Missing required fields", "details": "Amount, donation_type, and home_id are required"}), 400

        donation = donation_schema.load(data, session=db.session)
        db.session.add(donation)
        db.session.commit()
        return jsonify(donation_schema.dump(donation)), 201
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@donation_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_all_donations():
    try:
        donations = Donation.query.all()
        new_donations = [
            {
                "id": y.id,
                "amount": y.amount,
                "donation_type": y.donation_type,
                "user_id": y.user_id,
                "home_id": y.home_id,
                "created_at": y.created_at.isoformat()
            } for y in donations
        ]
        return jsonify(new_donations), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@donation_bp.route('/total', methods=['GET'])
@jwt_required()
def get_total_donations():
    try:
        total = db.session.query(func.sum(Donation.amount)).scalar() or 0
        return jsonify({"total_donations": total}), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500