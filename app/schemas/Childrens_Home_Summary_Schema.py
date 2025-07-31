# app/schemas/children_home_summary.py

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from app.models.children_home import ChildrenHome

class ChildrenHomeSummarySchema(SQLAlchemySchema):
    class Meta:
        model = ChildrenHome
        load_instance = True

    id = auto_field()
    name = auto_field()
    location = auto_field()
