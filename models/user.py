from init import db, ma 
from marshmallow import fields, Schema, validate, validates, ValidationError

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    location = db.relationship('Location', backref='users', lazy=True)
    allergies_model = db.relationship('Allergy', back_populates='user_model', overlaps="allergies,user_model")

class UserSchema(Schema):
    allergies = fields.List(fields.Nested('AllergySchema', exclude=['user']))
    restaurants = fields.List(fields.Nested('RestaurantSchema', exclude=['user']))
    first_name = fields.String(required=True, validate=validate.Length(min=1, max=30))
    last_name = fields.String(required=True, validate=validate.Length(min=1, max=30))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=30))

    @validates('first_name')
    def validate_first_name(self, value):
        if not value.isalpha():
            raise ValidationError('First name must only contain letters, no numbers or special characters.')

    class Meta:
        ordered = True
        fields = ('user_id', 'first_name', 'email', 'password', 'allergies', 'restaurants')


class UserProfileUpdate(Schema):
    first_name = fields.String(validate=validate.Length(min=1, max=30))
    last_name = fields.String(validate=validate.Length(min=1, max=30))
    email = fields.Email()
    password = fields.String(validate=validate.Length(min=8, max=30))
    allergies = fields.List(fields.Nested('AllergyUpdateSchema'))

    @validates('first_name')
    def validate_first_name(self, value):
        if not value.isalpha():
            raise ValidationError('First name must only contain letters, no spaces.')

class AllergyUpdateSchema(Schema):
    allergy_name = fields.String(validate=validate.Length(min=1, max=150))

    class Meta:
        ordered = True
        fields = ('id', 'allergy_name')