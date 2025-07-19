from app.__init__ import db
from datetime import datetime


class Volunteer(db.Model):
    __tablename__ = 'volunteers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    childrens_home = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
            "childrens_home": self.childrens_home,
            "description": self.description,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat()
        }



