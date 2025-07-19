from datetime import datetime
from app import db 

class Donation(db.Model):
    __tablename__ = 'donations'

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)
    donation_type = db.Column(db.String(20), nullable=False)  
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "donation_type": self.donation_type,
            "user_id": self.user_id,
            "home_id": self.home_id,
            "created_at": self.created_at.isoformat()
        }
