from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.children_home import ChildrenHome, Child, Photo
from app.schemas.home_schema import (
    childrenhome_schema,
    childrenhome_list_schema,
    child_list_schema,
    child_schema, 
    photo_list_schema
)
from app.utils.decorators import admin_required

home_bp = Blueprint("home_bp", __name__, url_prefix="/homes")



@home_bp.route("/<int:home_id>/photos", methods=["GET"])
# @jwt_required()
def get_photos_in_home(home_id):
    home = ChildrenHome.query.get_or_404(home_id)
    photos = Photo.query.filter_by(home_id=home.id).all()

    return jsonify(photo_list_schema.dump(photos)), 200


@home_bp.route("/", methods=["GET"])
# @jwt_required()
def get_homes():
    homes = ChildrenHome.query.all()
    return jsonify(childrenhome_list_schema.dump(homes)), 200


@home_bp.route("/<int:id>", methods=["GET"])
# @jwt_required()
def get_home(id):
    home = ChildrenHome.query.get_or_404(id)
    return jsonify(childrenhome_schema.dump(home)), 200



@home_bp.route("/", methods=["POST"])
# @jwt_required()
@admin_required
def create_home():
    data = childrenhome_schema.load(request.get_json())
    home = ChildrenHome(**data)
    db.session.add(home)
    db.session.commit()
    return jsonify(childrenhome_schema.dump(home)), 201


@home_bp.route("/<int:id>", methods=["PATCH"])
@jwt_required()
@admin_required
def update_home(id):
    home = ChildrenHome.query.get_or_404(id)
    updates = childrenhome_schema.load(request.get_json(), partial=True)
    for key, value in updates.items():
        setattr(home, key, value)
    db.session.commit()
    return jsonify(childrenhome_schema.dump(home)), 200


@home_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_home(id):
    home = ChildrenHome.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return jsonify({"message": "Children's Home deleted successfully"}), 204


@home_bp.route("/<int:id>/children", methods=["GET"])
@jwt_required()
@admin_required
def get_children_in_home(id):
    home = ChildrenHome.query.get_or_404(id)
    children = Child.query.filter_by(home_id=id).all()
    return jsonify(child_list_schema.dump(children)), 200


@home_bp.route("/<int:home_id>/children/<int:child_id>", methods=["GET"])
@jwt_required()
@admin_required
def get_child_record_in_home(home_id, child_id):
    home = ChildrenHome.query.get_or_404(home_id)

    child = Child.query.filter_by(id=child_id, home_id=home.id).first()
    if not child:
        return jsonify({"error": "Child not found in this home"}), 404

    return jsonify(child_schema.dump(child)), 200

