from init import db
from marshmallow import fields, Schema, validate, validates, ValidationError
from marshmallow.validate import Length

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    cities = db.relationship('City', back_populates='location', cascade='all, delete')
    location_id = db.Column(db.Integer, db.ForeignKey('citiy_id'), nullable=False)
    users = db.relationship('User', back_populates='location', foreign_keys=[location_id])

class LocationSchema(Schema):
    location_name = fields.String(required=True, validate=validate.Length(min=1, max=150))

    class Meta:
        ordered = True
        fields = ('location_id', 'location_name', 'user')