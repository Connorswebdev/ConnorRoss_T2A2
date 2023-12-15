from init import db, ma

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    street_number = db.Column(db.String(10))
    street_name = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    cuisine = db.Column(db.String(100))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)
    city = db.relationship('City', backref=db.backref('restaurants', lazy=True))


# JSON (de)serialization with Marshmallow
class RestaurantSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('restaurant_id', 'name', 'user')