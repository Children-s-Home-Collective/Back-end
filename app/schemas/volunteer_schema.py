from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.volunteer import Volunteer

class VolunteerSchema(SQLAlchemySchema):
    class Meta:
        model = Volunteer
        load_instance = True
        include_relationships = True

    id = auto_field(dump_only=True)

    # Remove load_only so these fields are serialized on output too
    name = auto_field(required=True)
    phone_number = auto_field(required=True)
    email = auto_field(required=True)
    description = auto_field(required=True)

    user_id = auto_field(dump_only=True)
    
    # Ensure home_id is included in both dump and load (default behavior)
    home_id = auto_field(required=True)

    created_at = auto_field(dump_only=True)

    user = fields.Nested("UserSchema", dump_only=True, many=True)


volunteer_schema=VolunteerSchema()
volunteer_list_schema=VolunteerSchema(many=True)