from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models.review import Review
from app.schemas.review_schema import review_schema
from marshmallow import ValidationError

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@review_bp.route('/', methods=['POST'])
@jwt_required()
def create_review():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        current_user_id = get_jwt_identity()
        data['user_id'] = current_user_id
        data.pop('id', None)

        if not all([data.get('rating'), data.get('home_id')]):
            return jsonify({"error": "Missing required fields", "details": "Rating and home_id are required"}), 400

        review = review_schema.load(data, session=db.session)
        db.session.add(review)
        db.session.commit()
        return jsonify(review_schema.dump(review)), 201
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@review_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_reviews():
    try:
        reviews = Review.query.all()
        new_reviews = [
            {
                "id": z.id,
                "rating": z.rating,
                "comment": z.comment,
                "user_id": z.user_id,
                "home_id": z.home_id,
                "created_at": z.created_at.isoformat()
            } for z in reviews
        ]
        return jsonify(new_reviews), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@review_bp.route('/home/<int:home_id>', methods=['GET'])
@jwt_required()
def get_reviews_for_home(home_id):
    try:
        reviews = Review.query.filter_by(home_id=home_id).all()

        if not reviews:
            return jsonify({"message": "No reviews found for this home."}), 404

        results = [
            {
                "id": review.id,
                "rating": review.rating,
                "comment": review.comment,
                "user_id": review.user_id,
                "home_id": review.home_id,
                "created_at": review.created_at.isoformat()
            }
            for review in reviews
        ]

        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500


@review_bp.route('/<int:review_id>', methods=['PUT'])
@jwt_required()
def update_review(review_id):
    try:
        current_user_id = get_jwt_identity()
        review = Review.query.get_or_404(review_id)
        if review.user_id != current_user_id:
            return jsonify({"error": "Unauthorized", "details": "You can only update your own reviews"}), 403

        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        data.pop('id', None)
        updated_review = review_schema.load(data, instance=review, session=db.session, partial=True)
        db.session.commit()
        return jsonify(review_schema.dump(updated_review)), 200
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@review_bp.route('/<int:review_id>', methods=['DELETE'])
@jwt_required()
def delete_review(review_id):
    try:
        current_user_id = get_jwt_identity()
        review = Review.query.get_or_404(review_id)
        if review.user_id != current_user_id:
            return jsonify({"error": "Unauthorized", "details": "You can only delete your own reviews"}), 403

        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": f"Review {review_id} deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500