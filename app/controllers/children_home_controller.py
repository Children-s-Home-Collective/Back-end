from flask import Blueprint, request, jsonify
from app import db
from app.models.children_home import ChildrenHome
from app.schemas.home_schema import (
    childrenhome_schema,
    childrenhome_list_schema
)

home_bp = Blueprint("home_bp", __name__, url_prefix= "/homes")


@home_bp.route("/", methods=["POST"])
def create_home():
    data=childrenhome_schema.load(request.get_json())
    home=ChildrenHome(**data)

    db.session.add(home)
    db.session.commit()
    return childrenhome_schema.jsonify(home), 201

@home_bp.route("/", methods=["GET"])
def get_homes():
    homes=ChildrenHome.query.all()
    return childrenhome_list_schema.jsonify(homes), 200

@home_bp.route("/<int:id>", methods=["GET"])
def get_home(id):
    home=ChildrenHome.query.get_or_404(id)
    return childrenhome_schema.jsonify(home), 200


@home_bp.route("/<int:id>", methods=["PATCH"])
def update_home(id):
    home=ChildrenHome.query.get_or_404(id)
    updates=childrenhome_schema.load(request.get_json(), partial=True)
    for key, value in updates.items():
        setattr(home, key, value)
    db.session.commit()
    return childrenhome_schema.jsonify(home), 200  

@home_bp.route("/<int:id>", methods=["DELETE"])
def delete_home(id):
    home=ChildrenHome.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    return jsonify({"message" : "Childrens' Home deleted"}), 204