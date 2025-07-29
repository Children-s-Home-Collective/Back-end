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
    photos = Photo.query.filter_by(children_home_id=home.id).all()

    return jsonify(photo_list_schema.dump(photos)), 200


@home_bp.route("/", methods=["GET"])
# @jwt_required()
def get_homes():
    # try:
    #     homes = ChildrenHome.query.all()
    #     results = []
    #     for home in homes:
    #         print(f"Home: {home.name}, Children type: {type(home.children)}, Children: {home.children}")
    #         results.append({
    #             "id": home.id,
    #             "name": home.name,
    #             "children": [
    #                 {
    #                     "id": child.id,
    #                     "first_name": child.first_name,
    #                     "last_name": child.last_name,
    #                     "age": child.age,
    #                     "gender": child.gender
    #                 } for child in home.children
    #             ]
    #         })
    #     return jsonify(results), 200
    # except Exception as e:
    #     print(f"Error in get_homes: {str(e)}")
    #     return jsonify({"error": "An error occurred"}), 500
    try:
        homes = ChildrenHome.query.all()
        results = []

        for home in homes:
            print(f"Home: {home.name}, Children count: {len(home.children)}, Photos count: {len(home.photos)}")

            home_data = {
                "id": home.id,
                "name": home.name,
                "location": home.location,
                "phone_number": home.phone_number,
                "email": home.email,
                "description": home.description,
                "created_at": home.created_at.isoformat(),
                "children": [
                    {
                        "id": child.id,
                        "first_name": child.first_name,
                        "last_name": child.last_name,
                        "age": child.age,
                        "gender": child.gender,
                        "created_at": child.created_at.isoformat()
                    } for child in home.children
                ],
                "photos": [
                    {
                        "id": photo.id,
                        "image_url": photo.image_url
                    } for photo in home.photos
                ]
            }

            results.append(home_data)

        return jsonify(results), 200

    except Exception as e:
        print(f"Error in get_homes: {str(e)}")
        return jsonify({"error": "An error occurred while fetching homes"}), 500
   




@home_bp.route("/<int:id>", methods=["GET"])
# @jwt_required()
def get_home(id):
    home = ChildrenHome.query.get_or_404(id)
    results = []
    home_data = {
                "id": home.id,
                "name": home.name,
                "location": home.location,
                "phone_number": home.phone_number,
                "email": home.email,
                "description": home.description,
                "created_at": home.created_at.isoformat(),
                "children": [
                    {
                        "id": child.id,
                        "first_name": child.first_name,
                        "last_name": child.last_name,
                        "age": child.age,
                        "gender": child.gender,
                        "created_at": child.created_at.isoformat()
                    } for child in home.children
                ],
                "photos": [
                    {
                        "id": photo.id,
                        "image_url": photo.image_url
                    } for photo in home.photos
                ]
            }

    results.append(home_data)

    return jsonify(results), 200



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
# @jwt_required()
# @admin_required
def get_children_in_home(id):
    home = ChildrenHome.query.get_or_404(id)
    children = Child.query.filter_by(home_id=home.id).all()
    results=[]
    for x in children:
        new={
                        "id": x.id,
                        "first_name": x.first_name,
                        "last_name": x.last_name,
                        "age": x.age,
                        "gender": x.gender,
                        "created_at": x.created_at.isoformat()
        },
        results.append(new)
    return jsonify(results), 200


@home_bp.route("/<int:home_id>/children/<int:child_id>", methods=["GET"])
# @jwt_required()
# @admin_required
def get_child_record_in_home(home_id, child_id):
    home = ChildrenHome.query.get_or_404(home_id)

    child = Child.query.filter_by(id=child_id, home_id=home.id).first()
    if not child:
        return jsonify({"error": "Child not found in this home"}), 404

    return jsonify(child_schema.dump(child)), 200

