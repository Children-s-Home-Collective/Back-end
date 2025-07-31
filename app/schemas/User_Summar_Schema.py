# app/schemas/user_summary.py

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.user import User

class UserSummarySchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    name = auto_field()
