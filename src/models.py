from datetime import datetime
from init import db
from flask_login import LoginManager, UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    allergies = db.relationship('Allergy', backref='user', lazy=True)

class Allergy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allergy_name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(255), nullable=False)
    cuisine_type = db.Column(db.String(100), nullable=False)