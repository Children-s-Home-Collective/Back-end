from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields, validate
from app.models.children_home import ChildrenHome, Child, Photo


class ChildSchema(SQLAlchemySchema):
    class Meta:
        model = Child
        load_instance = True

    id = auto_field(dump_only=True)
    first_name = auto_field(required=True)
    last_name = auto_field(required=True)
    age = auto_field(required=True)
    home_id = auto_field(dump_only=True)


class PhotoSchema(SQLAlchemySchema):
    class Meta:
        model = Photo
        load_instance = True

    id = auto_field(dump_only=True)
    image_url = auto_field(required=True)
    children_home_id = auto_field(dump_only=True)



class ChildrenHomeSchema(SQLAlchemySchema):
    class Meta:
        model = ChildrenHome
        load_instance = True
        include_relationships = True

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    location = auto_field(required=True)
    
    phone_number = auto_field(
        required=True,
        validate=validate.Length(min=10, max=13)
    )
    email = auto_field(
        required=False,
        validate=validate.Email(error="Invalid email address")
    )
    description = auto_field()
    created_at = auto_field(dump_only=True)

    
    images = fields.List(fields.Str(), required=True)   
    children_names = fields.List(fields.Str(), required=True)

  
    donations = fields.Nested("DonationSchema", many=True, dump_only=True)
    reviews = fields.Nested("ReviewSchema", many=True, dump_only=True)
    visits = fields.Nested("VisitSchema", many=True, dump_only=True)
    children = fields.Nested(ChildSchema, many=True, required=True)
    photos = fields.Nested(PhotoSchema, many=True, required=True)


child_schema = ChildSchema()
child_list_schema = ChildSchema(many=True)

photo_schema = PhotoSchema()
photo_list_schema = PhotoSchema(many=True)

childrenhome_schema = ChildrenHomeSchema()
childrenhome_list_schema = ChildrenHomeSchema(many=True)
