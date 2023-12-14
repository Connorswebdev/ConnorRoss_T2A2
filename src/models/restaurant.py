from init import db, ma

class Restaurant(db.Model):
    # Renames table to plural based on convention
    __tablename__ = 'restaurants'

    restaurant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    street_number = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    cuisine = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('User', backref=db.backref('restaurants', lazy=True))

    cities = db.relationship('City', back_populates='location', cascade='all, delete') #


# JSON (de)serialization with Marshmallow
class StateSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ('restaurant_id', 'name', 'user')