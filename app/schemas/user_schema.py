from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, fields
from app.models.user import User


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    
    email = fields.Email(required=True, 
                         validate=validate.Length(max=100))
    
    password = fields.String(load_only=True, 
                             required=True,
                             validate=validate.Length(min=8, max=255))
    
    role = auto_field(dump_only=True)  
    created_at = auto_field(dump_only=True)

    review=fields.Nested("ReviewSchema", many=True, dump_only=True)
    home=fields.Nested("ChildreHomeSchema", many=True, dump_only=True)
    donation=fields.Nested("DonationSchema", many=True, dump_only=True)
    visit=fields.Nested("VisitSchema", many=True, dump_only=True)
    volunteer=fields.Nested("VolunteerSchema", many=True, dump_only=True)

user_schema=UserSchema()
user_list_schema=UserSchema(many=True)    