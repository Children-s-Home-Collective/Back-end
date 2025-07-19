from datetime import datetime
from app import db  

class Visit(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    day_to_visit = db.Column(db.Date, nullable=False)
    number_of_visits = db.Column(db.Integer, default=1, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "phone_number": self.phone_number,
            "day_to_visit": self.day_to_visit.isoformat(),
            "number_of_visits": self.number_of_visits,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat()
        }
