from init import db, ma
from marshmallow import fields

class City(db.Model):
    __tablename__ = 'cities'
    city_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    location_relationship = db.relationship('Location', back_populates='cities', lazy=True)

# JSON (de)serialization with Marshmallow
class CitySchema(ma.Schema):
    location = fields.Nested('LocationSchema', exclude=['id'])

    class Meta:
        fields = ('city_id', 'name', 'postcode', 'location')