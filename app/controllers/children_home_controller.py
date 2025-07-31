from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app import db
from app.models.children_home import ChildrenHome, Child, Photo
from app.schemas.home_schema import (
    ChildrenHomeSchema,
    child_schema,
    photo_schema,
)
from app.utils.decorators import admin_required

home_bp = Blueprint("home_bp", __name__, url_prefix="/homes")

@home_bp.route("/<int:home_id>/photos", methods=["GET"])
@jwt_required()
def get_photos_in_home(home_id):
    try:
        home = ChildrenHome.query.get_or_404(home_id)
        photos = Photo.query.filter_by(children_home_id=home.id).all()
        results = sorted([{"id": photo.id, "image_url": photo.image_url} for photo in photos], key=lambda x: x["id"])
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:home_id>/photos/<int:photo_id>", methods=["GET"])
@jwt_required()
def get_a_single_photo_in_home(home_id, photo_id):
    try:
        home = ChildrenHome.query.get_or_404(home_id)
        photo = Photo.query.filter_by(id=photo_id, children_home_id=home.id).first()
        if not photo:
            return jsonify({"error": "Photo not found"}), 404
        return jsonify(photo_schema.dump(photo)), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/", methods=["GET"])
@jwt_required()
def get_homes():
    try:
        homes = ChildrenHome.query.all()
        results = [
            {
                "id": home.id,
                "name": home.name,
                "location": home.location,
                "phone_number": home.phone_number,
                "email": home.email,
                "description": home.description,
                "created_at": home.created_at.isoformat(),
                "children": sorted(
                    [
                        {
                            "id": child.id,
                            "first_name": child.first_name,
                            "last_name": child.last_name,
                            "age": child.age,
                            "gender": child.gender,
                            "created_at": child.created_at.isoformat()
                        } for child in home.children
                    ],
                    key=lambda x: x["id"]
                ),
                "photos": sorted(
                    [
                        {
                            "id": photo.id,
                            "image_url": photo.image_url
                        } for photo in home.photos
                    ],
                    key=lambda x: x["id"]
                )
            } for home in homes
        ]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_home(id):
    try:
        home = ChildrenHome.query.get_or_404(id)
        home_data = {
            "id": home.id,
            "name": home.name,
            "location": home.location,
            "phone_number": home.phone_number,
            "email": home.email,
            "description": home.description,
            "created_at": home.created_at.isoformat(),
            "children": sorted(
                [
                    {
                        "id": child.id,
                        "first_name": child.first_name,
                        "last_name": child.last_name,
                        "age": child.age,
                        "gender": child.gender,
                        "created_at": child.created_at.isoformat()
                    } for child in home.children
                    
                ],
                key=lambda x: x["id"]
            ),
            "photos": sorted(
                [
                    {
                        "id": photo.id,
                        "image_url": photo.image_url
                    } for photo in home.photos
                ],
                key=lambda x: x["id"]
            )
        }
        return jsonify([home_data]), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/", methods=["POST"])
@jwt_required()
@admin_required
def create_home():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        for field in ["id", "donations", "reviews", "visits", "created_at"]:
            data.pop(field, None)

        if "children" not in data or not data["children"]:
            return jsonify({"error": "Children required", "details": "At least one child is required"}), 400

        if "photos" not in data or not data["photos"]:
            return jsonify({"error": "Photos required", "details": "At least one photo is required"}), 400

        schema = ChildrenHomeSchema(session=db.session)
        home = schema.load(data, session=db.session)
        db.session.add(home)
        db.session.commit()
        for child in home.children:
            child.home_id = home.id
        db.session.commit()
        home_data = {
            "id": home.id,
            "name": home.name,
            "location": home.location,
            "phone_number": home.phone_number,
            "email": home.email,
            "description": home.description,
            "created_at": home.created_at.isoformat(),
            "children": sorted(
                [
                    {
                        "id": child.id,
                        "first_name": child.first_name,
                        "last_name": child.last_name,
                        "age": child.age,
                        "gender": child.gender,
                        "created_at": child.created_at.isoformat()
                    } for child in home.children
                ],
                key=lambda x: x["id"]
            ),
            "photos": sorted(
                [
                    {
                        "id": photo.id,
                        "image_url": photo.image_url
                    } for photo in home.photos
                ],
                key=lambda x: x["id"]
            )
        }
        return jsonify(home_data), 201
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_home(id):
    try:
        home = ChildrenHome.query.get_or_404(id)
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data", "details": "Request body is empty"}), 400

        for field in ["id", "donations", "reviews", "visits", "created_at"]:
            data.pop(field, None)

        if "children" in data and not data["children"]:
            return jsonify({"error": "Children required", "details": "Children list cannot be empty"}), 400

        if "photos" in data and not data["photos"]:
            return jsonify({"error": "Photos required", "details": "Photos list cannot be empty"}), 400

        schema = ChildrenHomeSchema(session=db.session)
        updated_home = schema.load(data, instance=home, session=db.session, partial=True)
        db.session.commit()

        home_data = {
            "id": updated_home.id,
            "name": updated_home.name,
            "location": updated_home.location,
            "phone_number": updated_home.phone_number,
            "email": updated_home.email,
            "description": updated_home.description,
            "created_at": updated_home.created_at.isoformat(),
            "children": sorted(
                [
                    {
                        "id": child.id,
                        "first_name": child.first_name,
                        "last_name": child.last_name,
                        "age": child.age,
                        "gender": child.gender,
                        "created_at": child.created_at.isoformat()
                    } for child in updated_home.children
                ],
                key=lambda x: x["id"]
            ),
            "photos": sorted(
                [
                    {
                        "id": photo.id,
                        "image_url": photo.image_url
                    } for photo in updated_home.photos
                ],
                key=lambda x: x["id"]
            )
        }
        return jsonify(home_data), 200
    except ValidationError as ve:
        return jsonify({"error": "Validation failed", "details": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_home(id):
    try:
        home = ChildrenHome.query.get_or_404(id)
        db.session.delete(home)
        db.session.commit()
        return jsonify({"message": "Home deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:id>/children", methods=["GET"])
@jwt_required()
@admin_required
def get_children_in_home(id):
    try:
        home = ChildrenHome.query.get_or_404(id)
        children = Child.query.filter_by(home_id=home.id).all()
        results = sorted(
            [
                {
                    "id": child.id,
                    "first_name": child.first_name,
                    "last_name": child.last_name,
                    "age": child.age,
                    "gender": child.gender,
                    "created_at": child.created_at.isoformat()
                } for child in children
            ],
            key=lambda x: x["id"]
        )
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500

@home_bp.route("/<int:home_id>/children/<int:child_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_child_record_in_home(home_id, child_id):
    try:
        home = ChildrenHome.query.get_or_404(home_id)
        child = Child.query.filter_by(id=child_id, home_id=home.id).first()
        if not child:
            return jsonify({"error": "Child not found"}), 404
        return jsonify(child_schema.dump(child)), 200
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500