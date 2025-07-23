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
    children = db.relationship('Child', backref='children_home', lazy=True, cascade='all, delete-orphan')
    photos = db.relationship('Photo', backref='children_home', lazy=True, cascade='all, delete-orphan')


    def __repr__(self):
     return f"<Home #{self.id}: {self.name} at {self.location}>"
    


class Child(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birth_certificate_number = db.Column(db.String(100), nullable=True)

    children_home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    def __repr__(self):
        return f"<Child #{self.id}: {self.full_name}, Age: {self.age}>"

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)

    children_home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    def __repr__(self):
        return f"<Photo #{self.id}: {self.image_url}>"

