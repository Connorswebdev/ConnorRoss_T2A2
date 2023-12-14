from flask import Blueprint, request
from init import db
from models.allergy import Allergy,  AllergySchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

# To add blueprint for allergies and define the prefix for all URLs in this blueprint
allergy_bp = Blueprint('allergies', __name__, url_prefix='/allergies')

# The following are CRUD routes for allergies

# READ: Route for getting a list of all allergies
@allergy_bp.route('/')
def all_allergies():
    stmt = db.select(Allergy)
    allergies = db.session.scalars(stmt).all()
    return AllergySchema(many=True, exclude=['Location_id']).dump(allergies) # Location id is excluded as Location name will be returned anyway


# READ: Route for getting the information of one allergy, specified by the allergy id in the URL in integer form
@allergy_bp.route('/<int:allergy_id>')
def one_allergy(allergy_id):
    stmt = db.select(allergy).filter_by(id=allergy_id)
    allergy = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if allergy:
        return AllergySchema(exclude=['id', 'Location_id']).dump(allergy) # allergy id is already in the URL, and Location id is excluded as Location name will be returned
    else:
        return {'error': 'allergy not found'}, 404 # Handles error of invalid allergy id with a clear error message
    

# CREATE: Route for creating a new allergy, with login required
@allergy_bp.route('/', methods=['POST'])
@jwt_required() # Only existing users can create new allergies
def create_allergy():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        allergy_info = AllergySchema().load(request.json)

        # Create a new allergy model instance with the schema data
        allergy = allergy(
            allergy_name = allergy_info['allergy_name'],
        )

        db.session.add(allergy)
        db.session.commit() # Finalising the addition of the new allergy to the database

        return AllergySchema(exclude=['Location_id']).dump(allergy), 201 # Location id is excluded as Location name will be returned anyway
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# UPDATE: Modifying a allergy's information, with the id in the URL, login required.
@allergy_bp.route('/<int:allergy_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Only existing users can modify allergy information
def update_allergy(allergy_id):
    try:
        stmt = db.select(allergy).filter_by(id=allergy_id)
        allergy = db.session.scalar(stmt)
        allergy_info = AllergySchema().load(request.json) # Applies validation rules in schema
        if allergy:
            allergy.name = allergy_info.get('name', allergy.name) # This is optional. If not entered, then the original value will be kept.
            db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
            return AllergySchema()
        else:
            return {'error': 'allergy not found'}, 404 # Handles error of invalid allergy id with a clear error message
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# DELETE: Removing a allergy, with the id in the URL, login required.
@allergy_bp.route('/<int:allergy_id>', methods=['DELETE'])
@jwt_required() # Only existing users can delete allergies
def delete_allergy(allergy_id):
    stmt = db.select(allergy).filter_by(id=allergy_id)
    allergy = db.session.scalar(stmt)
    if allergy:
       db.session.delete(allergy)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the allergy was removed, with a 200 success response
    else:
       return {'error': 'allergy not found'}, 404 # Handles error of invalid allergy id with a clear error message