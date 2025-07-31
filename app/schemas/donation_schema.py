from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from app.models.donation import Donation
from app.schemas.Childrens_Home_Summary_Schema import ChildrenHomeSummarySchema
from app.schemas.User_Summar_Schema import UserSummarySchema

class DonationSchema(SQLAlchemySchema):

    class Meta:
        model= Donation
        load_instance= True
        include_relationships= True


    id= auto_field(dump_only=True)

    amount= auto_field(load_only=True)
    donation_type=auto_field(load_only=True)

    user_id =auto_field(dump_only=True)

    home_id=auto_field(required=True)


    created_at=auto_field(dump_only=True)

    home=fields.Nested("ChildrenHomeSummarySchema", dump_only=True)
    user=fields.Nested("UserSummarySchema", dump_only=True)

donation_schema=DonationSchema()
donation_list_schema=DonationSchema(many=True)