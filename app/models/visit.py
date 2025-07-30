from datetime import datetime, timezone
from app import db  

class Visit(db.Model):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    full_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    day_to_visit = db.Column(db.Date, nullable=False)
    number_of_visitors = db.Column(db.Integer, default=1, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
     return (
        f"<Visit #{self.id}: {self.full_name} visiting home {self.home_id} "
        f"on {self.day_to_visit.strftime('%Y-%m-%d')}>"
    )
