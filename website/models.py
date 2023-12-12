from datetime import datetime
from website.extensions import db
from website import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __table__ = db.Table('user', db.metadata, extend_existing=True, autoload = True, autoload_with=db.engine)
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    allergies = db.relationship('Allergy', backref='user', lazy=True)

class Allergy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allergy_name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(255), nullable=False)
    cuisine_type = db.Column(db.String(100), nullable=False)