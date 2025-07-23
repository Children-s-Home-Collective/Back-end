from datetime import datetime
from app import db 

class ChildrenHome(db.Model):
    __tablename__ = 'children_homes'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

   
    donations = db.relationship('Donation', backref='children_home', lazy=True)
    reviews = db.relationship('Review', backref='children_home', lazy=True)
    visits = db.relationship('Visit', backref='children_home', lazy=True)

    def __repr__(self):
     return f"<Home #{self.id}: {self.name} at {self.location}>"
