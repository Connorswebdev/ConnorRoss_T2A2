from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    allergies = db.relationship('Allergy', backref='user', lazy=True)

class Allergy(db.Model):
    id = db.Column(db.integer, primary_key=True)
    allergy_name = db.Column(db.string(50), nullable=False)
    user_id = db.Column(db.integer, db.foreign_key('user.id'), nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.integer, primary_key=True)
    restaurant_name = db.Column(db.String(255), nullable=False)
    cuisine_type = db.Column(db,string(100), nullable=False)