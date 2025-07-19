from datetime import datetime
from app import db 

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    rating = db.Column(db.Integer, nullable=False) 
    comment = db.Column(db.Text, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "comment": self.comment,
            "user_id": self.user_id,
            "home_id": self.home_id,
            "created_at": self.created_at.isoformat()
        }
