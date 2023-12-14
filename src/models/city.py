from init import db, ma
from marshmallow import fields

# SQLAlchemy creates table structure with columns and data types
class City(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.Integer, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.id', ondelete='CASCADE'), nullable=False)
    location = db.relationship('location', back_populates='cities') # 
    venues = db.relationship('Venue', back_populates='city', cascade='all, delete')

# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    location = fields.Nested('locationSchema', exclude=['id'])

    class Meta:
        fields = ('id', 'name', 'postcode', 'location')