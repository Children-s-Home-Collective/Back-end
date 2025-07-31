from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import validate, fields
from app.models.user import User


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        include_fk=True
        exclude = ["password"]


    id = auto_field(dump_only=True)
    name = auto_field(required=True)
    
    email = fields.Email(required=True, 
                         validate=validate.Length(max=100))
    phone_number=fields.Str(validate=validate.Regexp(r"^(?:\+|0)[0-9]{9,12}$"))
    
    password = fields.String(load_only=True, 
                             required=True,
                            validate=[
           validate.Length(min=8, error="Password must be at least 8 characters long."),
           validate.Regexp(r".*[\W_]", error="Password must include at least one special character."),
           validate.Regexp(r".*[0-9]", error="Password must include at least one digit."),
        ] )
    
    role = auto_field(dump_only=True)  
    created_at = auto_field(dump_only=True)

    review=fields.Nested("ReviewSchema", many=True, dump_only=True)
    home=fields.Nested("ChildrenHomeSchema", many=True, dump_only=True)
    donation=fields.Nested("DonationSchema", many=True, dump_only=True ,exclude=("user",))
    visit=fields.Nested("VisitSchema", many=True, dump_only=True)
    volunteer=fields.Nested("VolunteerSchema", many=True, dump_only=True)

user_schema=UserSchema()
user_list_schema=UserSchema(many=True)    