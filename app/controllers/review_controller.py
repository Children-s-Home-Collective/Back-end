from flask import Blueprint, request, jsonify
from app import db
from app.models.review import Review  
from app.schemas.review_schema import review_schema, review_list_schema

review_bp = Blueprint('reviews', __name__, url_prefix='/reviews')



@review_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    try:
        review = review_schema.load(data, session=db.session)
        db.session.add(review)
        db.session.commit()
        return review_schema.jsonify(review), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@review_bp.route('/', methods=['GET'])
def get_all_reviews():
    reviews = Review.query.all()
    new_reviews=[]
    for z in reviews:
        news={
            "id":z.id,
            "rating":z.rating,
            "comment":z.comment,
            "user_id":z.user_id,
            "home_id":z.home_id,
            "created_at":z.created_at
        }
        new_reviews.append(news)
    return jsonify(new_reviews), 200



@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get_or_404(review_id)
    new_review={
            "id":review.id,
            "rating":review.rating,
            "comment":review.comment,
            "user_id":review.user_id,
            "home_id":review.home_id,
            "created_at":review.created_at       
    }
    return jsonify(new_review), 200



@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.get_json()
    if not json_data:
        return jsonify({"error": "Missing JSON in request"}), 400

    review = Review.query.get_or_404(review_id)

    try:
        updated_data = review_schema.load(data, instance=review, session=db.session, partial=True)

        db.session.commit()
        return review_schema.jsonify(updated_data), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400



@review_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": f"Review {review_id} deleted"}), 200
