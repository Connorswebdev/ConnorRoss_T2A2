from init import db
from marshmallow import fields, Schema, validate

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(150), nullable=False)
    cities = db.relationship('City', backref='location', lazy=True)
    users = db.relationship('User', back_populates='location', lazy=True)
    

class LocationSchema(Schema):
    location_id = fields.Integer(dump_only=True)
    location_name = fields.String(required=True, validate=validate.Length(min=1, max=150))

    class Meta:
        ordered = True
        fields = ('location_id', 'location_name', 'cities')