from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.visit import Visit
from app.schemas.Childrens_Home_Summary_Schema import ChildrenHomeSummarySchema  # Import the summary schemas
from app.schemas.User_Summar_Schema import UserSummarySchema

class VisitSchema(SQLAlchemySchema):
    class Meta:
        model = Visit
        load_instance = True
        include_relationships = True
        include_fk = True

    id = auto_field(dump_only=True)
    full_name = auto_field(required=True)
    phone_number = auto_field(required=True)
    day_to_visit = auto_field(required=True)
    number_of_visitors = auto_field(required=True)

    user_id = auto_field(dump_only=True)
    home_id = auto_field(required=True)

    created_at = auto_field(dump_only=True)

    home = fields.Nested(ChildrenHomeSummarySchema, dump_only=True)
    user = fields.Nested(UserSummarySchema, dump_only=True)

visit_schema = VisitSchema()
visit_list_schema = VisitSchema(many=True)
