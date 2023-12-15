from flask import Blueprint, request
from init import db
from models.restaurant import Restaurant, RestaurantSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

# To add blueprint for restaurants and define the prefix for all URLs in this blueprint
restaurants_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

# The following are CRUD routes for restaurants

# READ: Route for getting a list of all restaurants
@restaurants_bp.route('/')
def all_restaurants():
    stmt = db.select(restaurants)
    restaurants = db.session.scalars(stmt).all()
    return RestaurantSchema(many=True, exclude=['location_id']).dump(restaurants) # Location id is excluded as Location name will be returned anyway


# READ: Route for getting the information of one restaurant, specified by the restaurant id in the URL in integer form
@restaurants_bp.route('/<int:restaurant_id>')
def one_restaurant(restaurant_id):
    stmt = db.select(restaurant).filter_by(id=restaurant_id)
    restaurant = db.session.scalar(stmt) # Singular scalar as only one instance is expected
    if restaurant:
        return RestaurantSchema(exclude=['id', 'location_id']).dump(restaurant) # restaurant id is already in the URL, and Location id is excluded as Location name will be returned
    else:
        return {'error': 'restaurant not found'}, 404 # Handles error of invalid restaurant id with a clear error message
    

# CREATE: Route for creating a new restaurant, with login required
@restaurants_bp.route('/', methods=['POST'])
@jwt_required() # Only existing users can create new restaurants
def create_restaurant():
    try:
        # Parse, sanitize and validate the incoming JSON data via the schema
        restaurant_info = RestaurantSchema().load(request.json)

        # Create a new restaurant model instance with the schema data
        restaurant = restaurant(
            name = restaurant_info['name'],
            street_number = restaurant_info['street_number'],
            street_name = restaurant_info['street_name'],
            phone = restaurant_info['phone'],
            email = restaurant_info['email'],
            description = restaurant_info.get('description'), # This is optional. If not entered, will be null.
            cuisine = restaurant_info.get('cuisine'), # This is optional. If not entered, will be null.
            location_id = restaurant_info['location_id']
        )

        db.session.add(restaurant)
        db.session.commit() # Finalising the addition of the new restaurant to the database

        return RestaurantSchema(exclude=['location_id']).dump(restaurant), 201 # Location id is excluded as Location name will be returned anyway
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# UPDATE: Modifying a restaurant's information, with the id in the URL, login required.
@restaurants_bp.route('/<int:restaurant_id>', methods=['PUT', 'PATCH'])
@jwt_required() # Only existing users can modify restaurant information
def update_restaurant(restaurant_id):
    try:
        stmt = db.select(restaurant).filter_by(id=restaurant_id)
        restaurant = db.session.scalar(stmt)
        restaurant_info = RestaurantSchema().load(request.json) # Applies validation rules in schema
        if restaurant:
            restaurant.name = restaurant_info.get('name', restaurant.name) # This, and the following rows, are all optional. If not entered, then the original value will be kept.
            restaurant.street_number = restaurant_info.get('street_number', restaurant.street_number)
            restaurant.street_name = restaurant_info.get('street_name', restaurant.street_name)
            restaurant.phone = restaurant_info.get('phone', restaurant.phone)
            restaurant.email = restaurant_info.get('email', restaurant.email)
            restaurant.description = restaurant_info.get('description', restaurant.description)
            restaurant.location_id = restaurant_info.get('location_id', restaurant.location_id)
            db.session.commit() # Finalizing the change in the database, don't need to add session as nothing new was created
            return RestaurantSchema(exclude=['location_id']).dump(restaurant) # Location id is excluded as Location name will be returned anyway
        else:
            return {'error': 'restaurant not found'}, 404 # Handles error of invalid restaurant id with a clear error message
    except IntegrityError: # Integrity error in a try except block, handles invalid Location id with a clear error message.
        return {'error': 'Location ID does not exist.'}, 400


# DELETE: Removing a restaurant, with the id in the URL, login required.
@restaurants_bp.route('/<int:restaurant_id>', methods=['DELETE'])
@jwt_required() # Only existing users can delete restaurants
def delete_restaurant(restaurant_id):
    stmt = db.select(restaurant).filter_by(id=restaurant_id)
    restaurant = db.session.scalar(stmt)
    if restaurant:
       db.session.delete(restaurant)
       db.session.commit() # Finalising the deletion in the database
       return{}, 200 # Nothing returned as the restaurant was removed, with a 200 success response
    else:
       return {'error': 'restaurant not found'}, 404 # Handles error of invalid restaurant id with a clear error message