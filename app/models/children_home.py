from datetime import datetime, timezone
from app import db


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
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('children_homes.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


    def __repr__(self):
        return f"<Child #{self.id}: {self.first_name} {self.last_name} ({self.gender}, {self.age})>"



class ChildrenHome(db.Model):
    __tablename__ = 'children_homes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    donations = db.relationship('Donation', backref=db.backref('home', lazy=True), lazy=True, cascade='all, delete-orphan')
    reviews = db.relationship('Review', backref=db.backref('home', lazy=True), lazy=True, cascade='all, delete-orphan')
    visits = db.relationship('Visit', backref=db.backref('home', lazy=True), lazy=True, cascade='all, delete-orphan')
    children = db.relationship(Child, backref=db.backref('home', lazy=True), lazy=True, cascade='all, delete-orphan')
    photos = db.relationship(Photo, backref=db.backref('home', lazy=True), lazy=True, cascade='all, delete-orphan')

    @property
    def images(self):
        return [photo.image_url for photo in self.photos]

    @property
    def children_names(self):
        return [f"{child.first_name} {child.last_name}" for child in self.children]

    def __repr__(self):
        return f"<Home #{self.id}: {self.name} at {self.location}>"