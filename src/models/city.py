from init import db, ma
from marshmallow import fields

class City(db.Model):
    __tablename__ = 'cities'

    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    postcode = db.Column(db.String(10), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    location = db.relationship('Location', back_populates='cities')

# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    location = fields.Nested('LocationSchema', exclude=['id'])

    class Meta:
        fields = ('id', 'name', 'postcode', 'location')