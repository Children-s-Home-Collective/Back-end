from flask import Blueprint, request, jsonify
from app import db
from models.review import review  

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')



@review_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    try:
        new_review = review(
            rating=data['rating'],
            comment=data.get('comment'),
            user_id=data['user_id'],
            home_id=data['home_id']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@review_bp.route('/', methods=['GET'])
def get_all_reviews():
    reviews = review.query.all()
    return jsonify([review.serialize() for review in reviews]), 200



@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = review.query.get_or_404(review_id)
    return jsonify(review.serialize()), 200



@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    review = review.query.get_or_404(review_id)

    try:
        review.rating = data.get('rating', review.rating)
        review.comment = data.get('comment', review.comment)
        review.user_id = data.get('user_id', review.user_id)
        review.home_id = data.get('home_id', review.home_id)

        db.session.commit()
        return jsonify(review.serialize()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Review {review_id} deleted"}), 200
