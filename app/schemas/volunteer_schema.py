from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.volunteer import Volunteer

class VolunteerSchema(SQLAlchemySchema):
    class Meta:
        model = Volunteer
        load_instance = True
        include_relationships = True

    id=auto_field(dump_only=True)

    name=auto_field(load_only=True, required=True)
    phone_number=auto_field(load_only=True, required=True) 
    email=auto_field(required=True)
    description=auto_field(required=True)

    user_id=auto_field(dump_only=True)
    home_id=auto_field(dump_only=True)

    created_at=auto_field(dump_only=True)

    user=fields.Nested("UserSchema", dump_only=True, many=True)

volunteer_schema=VolunteerSchema()
volunteer_list_schema=VolunteerSchema(many=True)