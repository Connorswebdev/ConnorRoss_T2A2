from flask import Blueprint, request
from init import db
from models.restaurant import Restaurant, RestaurantSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

# To add blueprint for Restaurants and define the prefix for all URLs in this blueprint
restaurants_bp = Blueprint('Restaurants', __name__, url_prefix='/Restaurants')

# The following are CRUD routes for Restaurants

# READ: Route for getting a list of all Restaurants
@restaurants_bp.route('/')
def all_Restaurants():
    stmt = db.select(Restaurant)
    Restaurants = db.session.scalars(stmt).all()
    return RestaurantSchema(many=True, exclude=['Location_id']).dump(Restaurants) # Location id is excluded as Location name will be returned anyway


# READ: Route for getting the information of one Restaurant, specified by the Restaurant id in the URL in integer form
@restaurants_bp.route('/<int:Restaurant_id>')
def one_Restaurant(Restaurant_id):
    stmt = db.select(Restaurant).filter_by(id=Restaurant_id)
    Restaurant = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if Restaurant:
        return RestaurantSchema(exclude=['id', 'Location_id']).dump(Restaurant) # Restaurant id is already in the URL, and Location id is excluded as Location name will be returned
    else:
        return {'error': 'Restaurant not found'}, 404 # Handles error of invalid Restaurant id with a clear error message
    

# CREATE: Route for creating a new Restaurant, with login required
@restaurants_bp.route('/', methods=['POST'])
@jwt_required() # Only existing users can create new Restaurants
def create_Restaurant():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        Restaurant_info = RestaurantSchema().load(request.json)

        # Create a new Restaurant model instance with the schema data
        Restaurant = Restaurant(
            name = Restaurant_info['name'],
            street_number = Restaurant_info['street_number'],
            street_name = Restaurant_info['street_name'],
            phone = Restaurant_info['phone'],
            email = Restaurant_info['email'],
            description = Restaurant_info.get('description'), # This is optional. If not entered, will be null.
            cuisine = Restaurant_info.get('cuisine'), # This is optional. If not entered, will be null.
            Location_id = Restaurant_info['Location_id']
        )

        db.session.add(Restaurant)
        db.session.commit() # Finalising the addition of the new Restaurant to the database

        return RestaurantSchema(exclude=['Location_id']).dump(Restaurant), 201 # Location id is excluded as Location name will be returned anyway
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# UPDATE: Modifying a Restaurant's information, with the id in the URL, login required.
@restaurants_bp.route('/<int:Restaurant_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Only existing users can modify Restaurant information
def update_Restaurant(Restaurant_id):
    try:
        stmt = db.select(Restaurant).filter_by(id=Restaurant_id)
        Restaurant = db.session.scalar(stmt)
        Restaurant_info = RestaurantSchema().load(request.json) # Applies validation rules in schema
        if Restaurant:
            Restaurant.name = Restaurant_info.get('name', Restaurant.name) # This, and the following rows, are all optional. If not entered, then the original value will be kept.
            Restaurant.street_number = Restaurant_info.get('street_number', Restaurant.street_number)
            Restaurant.street_name = Restaurant_info.get('street_name', Restaurant.street_name)
            Restaurant.phone = Restaurant_info.get('phone', Restaurant.phone)
            Restaurant.email = Restaurant_info.get('email', Restaurant.email)
            Restaurant.description = Restaurant_info.get('description', Restaurant.description)
            Restaurant.Location_id = Restaurant_info.get('Location_id', Restaurant.Location_id)
            db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
            return RestaurantSchema(exclude=['Location_id']).dump(Restaurant) # Location id is excluded as Location name will be returned anyway
        else:
            return {'error': 'Restaurant not found'}, 404 # Handles error of invalid Restaurant id with a clear error message
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# DELETE: Removing a Restaurant, with the id in the URL, login required.
@restaurants_bp.route('/<int:Restaurant_id>', methods=['DELETE'])
@jwt_required() # Only existing users can delete Restaurants
def delete_Restaurant(Restaurant_id):
    stmt = db.select(Restaurant).filter_by(id=Restaurant_id)
    Restaurant = db.session.scalar(stmt)
    if Restaurant:
       db.session.delete(Restaurant)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the Restaurant was removed, with a 200 success response
    else:
       return {'error': 'Restaurant not found'}, 404 # Handles error of invalid Restaurant id with a clear error message