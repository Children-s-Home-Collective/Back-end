from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Donation
from app.schemas.donation_schema import donation_schema, donation_list_schema
from app.utils.decorators import admin_required
from sqlalchemy import func


donation_bp = Blueprint('donation_bp', __name__, url_prefix="donations")

@donation_bp.route('/', methods=['POST'])
@jwt_required()
def create_donation():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    
    data['user_id'] = current_user_id
    donation = donation_schema.load(data)

    db.session.add(donation)
    db.session.commit()

    return donation_schema.jsonify(donation), 201

@donation_bp.route('/', methods=['GET'])
@jwt_required()
@admin_required
def get_all_donations():
    donations = Donation.query.all()
    return donation_list_schema.jsonify(donations), 200

@donation_bp.route('/total', methods=['GET'])
def get_total_donations():
    total = db.session.query(func.sum(Donation.amount)).scalar() or 0
    return jsonify({"total_donations": total}), 200
