from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, fields
from app.models.review import Review

class ReviewSchema(SQLAlchemySchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True 
        include_relationships = True

    id=auto_field(dump_only=True)

    rating=auto_field(load_only=True)
    comment=auto_field(load_only=True) 

    user_id=auto_field(dump_only=True)
    home_id=auto_field(required=True)

    created_at=auto_field(dump_only=True)

    home=fields.Nested("ChildrenHomeSchema", dump_only=True)
    user=fields.Nested("UserSchema", dump_only=True)

review_schema=ReviewSchema()
review_list_schema=ReviewSchema(many=True)
