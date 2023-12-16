from init import db, ma

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    street_number = db.Column(db.String(10), nullable=False)
    street_name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)  # Update this line
    def __repr__(self):
        return f"<Restaurant {self.name}>"

# JSON (de)serialization with Marshmallow
class RestaurantSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('restaurant_id', 'name', 'user')