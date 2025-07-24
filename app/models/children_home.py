from datetime import datetime
from app import db 
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.hybrid import hybrid_property


class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)

    children_home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    def __repr__(self):
        return f"<Photo #{self.id}: {self.image_url}>"
    
class Child(db.Model):
    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Child #{self.id}: {self.first_name },{self.last_name}({self.gender}, {self.age})>"


class ChildrenHome(db.Model):
    __tablename__ = 'children_homes'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)
    images = db.Column(ARRAY(db.String)) 

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    @hybrid_property
    def images(self):
        return [photo.image_url for photo in self.photos]

    @hybrid_property
    def children_names(self):
        return [child.name for child in self.children]
   
    donations = db.relationship('Donation', lazy=True)
    reviews = db.relationship('Review', lazy=True)
    visits = db.relationship('Visit', lazy=True)
    children = db.relationship(Child, lazy=True, cascade='all, delete-orphan')
    photos = db.relationship(Photo, lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
     return f"<Home #{self.id}: {self.name} at {self.location}>"
    