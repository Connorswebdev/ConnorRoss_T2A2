from init import db
from marshmallow import fields, Schema, validate, validates, ValidationError
from marshmallow.validate import Length

class Allergy(db.Model):
    __tablename__ = 'allergies'
    id = db.Column(db.Integer, primary_key=True)
    allergy_name = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('User', backref=db.backref('allergies', lazy=True))


class AllergySchema(Schema):
    allergy_name = fields.String(required=True, validate=validate.Length(min=1, max=150))

    class Meta:
        ordered = True
        fields = ('id', 'allergy_name', 'user')