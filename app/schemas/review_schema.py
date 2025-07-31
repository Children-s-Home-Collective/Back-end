from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields, validate
from app.models.review import Review
from app.schemas.User_Summary_Schema import UserSummarySchema
from app.schemas.Children_Home_Summary_Schema import ChildrenHomeSummarySchema

class ReviewSchema(SQLAlchemySchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)

    rating = fields.Integer(
        required=True,
        validate=validate.Range(min=1, max=5, error="Rating must be between 1 and 5")
    )
    comment = fields.String(required=True)

    user_id = auto_field(dump_only=True)
    home_id = auto_field(required=True)

    created_at = auto_field(dump_only=True)

    home = fields.Nested(ChildrenHomeSummarySchema, dump_only=True)
    user = fields.Nested(UserSummarySchema, dump_only=True)

review_schema = ReviewSchema()
review_list_schema = ReviewSchema(many=True)
