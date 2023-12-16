from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.allergy import Allergy
from models.restaurant import Restaurant
from models.city import City, Location

cli_bp = Blueprint('db', __name__)

# Command to create database tables based on the imported models
@cli_bp.cli.command("create")
def create_db():
    db.drop_all()  # Drop any existing tables to ensure a clean slate
    db.create_all()
    print("Tables created successfully")

# Command to seed data into the database
@cli_bp.cli.command("seed")
def seed_db():
    # Seed Location data
    locations = [
        Location(name='Brisbane'),
        Location(name='Sydney'),
        Location(name='Adelaide'),
        Location(name='Perth'),
        Location(name='Hobart')
    ]

    db.session.query(Location).delete()  # Delete any existing locations data first to avoid unexpected results
    db.session.add_all(locations)
    db.session.commit()  # Locations are committed

    # Fetch the locations again after committing to get their IDs
    locations = Location.query.all()

    # Seed City data with valid location_ids
    cities = [
        City(name='Brisbane', postcode='4173', location_id=locations[0].location_id),  # Link to Brisbane location
        City(name='Sydney', postcode='2304', location_id=locations[1].location_id),    # Link to Sydney location
        City(name='Adelaide', postcode='0810', location_id=locations[2].location_id),  # Link to Adelaide location
        City(name='Perth', postcode='6148', location_id=locations[3].location_id),      # Link to Perth location
        City(name='Hobart', postcode='5082', location_id=locations[4].location_id)      # Link to Hobart location
    ]

    db.session.query(City).delete()  # Delete any existing cities data first to avoid unexpected results
    db.session.add_all(cities)
    db.session.commit()  # Cities are committed

    # Fetch the locations again after committing to get their IDs
    locations = City.query.all()

    # Seed User data with valid location_ids and allergies
    users = [
        User(
            first_name='admin',
            last_name='admin',
            email='admin@dineandwine.com',
            password=bcrypt.generate_password_hash('admin123%').decode('utf-8'),
            location_id=locations[0].location_id
        ),
        User(
            first_name='John',
            last_name='Doe',
            email='hello@fakeemail.com',
            password=bcrypt.generate_password_hash('Johndoe1!').decode('utf-8'),
            location_id=locations[1].location_id
        ),
        User(
            first_name='Robin',
            last_name='Banks',
            email='idonotrobbanks@mymail.com',
            password=bcrypt.generate_password_hash('iluvmoney!').decode('utf-8'),
            location_id=locations[2].location_id
        )
    ]

    # Create instances of Allergy separately
    allergies = [
        Allergy(allergy_name='None', user_id=users[0].user_id),
        Allergy(allergy_name='Nuts', user_id=users[1].user_id),
        Allergy(allergy_name='Gluten', user_id=users[2].user_id)
    ]
    for i, user in enumerate(users):
        user_id = db.session.query(User.user_id).filter_by(email=user.email).scalar()
    allergies[i].user_id = user_id
    user.allergies = [allergies[i]]
    # Associate allergies with users
    users[0].allergies = [allergies[0]]
    users[1].allergies = [allergies[1]]
    users[2].allergies = [allergies[2]]

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    db.session.query(Allergy).delete()
    db.session.add_all(allergies)
    db.session.commit()

    # Fetch the locations again after committing to get their IDs
    locations = City.query.all()

    restaurants = [
        Restaurant(
            name='Lemoni Greek Cuzina',
            street_number='1795',
            street_name='Wynnum Rd',
            phone='0733905505',
            email='bookings@lemoni.com.au',
            cuisine='Greek',
            city_id=locations[0].city_id
        ),
        Restaurant(
            name='Pho Bistro & Grill',
            street_number='348',
            street_name='Bagot Rd',
            phone='(08) 8981 4914',
            email='phobistrodarwin@gmail.com',
            cuisine='Vietnamese',
            city_id=locations[3].city_id
        ),
        Restaurant(
            name='Stax Burger Co.',
            street_number='98',
            street_name='Prospect Rd',
            phone='(08) 8344 5873',
            email='hello@staxburger.com',
            cuisine='American',
            city_id=locations[4].city_id
        )
    ]

    db.session.query(Restaurant).delete()  # Delete any existing restaurant data first to avoid unexpected results
    db.session.add_all(restaurants)
    db.session.commit()  # Final commit to add restaurants to the database

    print("Models seeded")