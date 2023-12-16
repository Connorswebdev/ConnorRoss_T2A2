from init import db, ma
from marshmallow import fields

class City(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id', ondelete='CASCADE'), nullable=False)
    location = db.relationship('Location', backref='cities', lazy=True)
    restaurants = db.relationship('Restaurant', backref='city', lazy=True)


class Location(db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    location = fields.Nested('LocationSchema', exclude=['id'])

    class Meta:
        fields = ('city_id', 'name', 'postcode', 'location')


class LocationSchema(ma.Schema):

    class Meta:
        fields = ('location_id', 'name')
