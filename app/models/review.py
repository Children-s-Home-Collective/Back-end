from datetime import datetime, timezone
from app import db 

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    rating = db.Column(db.Integer, nullable=False) 
    comment = db.Column(db.Text, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

def __repr__(self):
        return f"<Review #{self.id}: {self.rating}★ by user {self.user_id} on home {self.home_id}>"