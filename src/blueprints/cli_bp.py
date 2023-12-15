from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.allergy import Allergy
from models.restaurant import Restaurant
from models.city import City

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
    # Seed User data
    users = [
        User(
            first_name='admin',
            last_name='admin',
            email='admin@dineandwine.com',
            password=bcrypt.generate_password_hash('admin123%').decode('utf-8'),
            allergies='None',
            is_admin=True
        ),
        User(
            first_name='John',
            last_name='Doe',
            email='hello@fakeemail.com',
            password=bcrypt.generate_password_hash('Johndoe1!').decode('utf-8'),
            allergies='Nuts',
            is_admin=False
        ),
        User(
            first_name='Robin',
            last_name='Banks',
            email='idonotrobbanks@mymail.com',
            password=bcrypt.generate_password_hash('iluvmoney!').decode('utf-8'),
            allergies='Gluten',
            is_admin=False
        )
    ]

    # Delete existing User data to avoid unexpected results
    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    # Only select cities are added here for demonstration purposes
    cities = [
        City(
            name='Tingalpa',
            postcode='4173',
            location_name='Brisbane'  # Adding location information directly to the city
        ),
        City(
            name='Mayfield',
            postcode='2304',
            location_name='Sydney'
        ),
        City(
            name='Cocount Grove',
            postcode='0810',
            location_name='Adelaide'
        ),
        City(
            name='Riverton',
            postcode='6148',
            location_name='Perth'
        ),
        City(
            name='Prospect',
            postcode='5082',
            location_name='Hobart'
        )
    ]

    db.session.query(City).delete()  # Delete any existing cities data first to avoid unexpected results
    db.session.add_all(cities)
    db.session.commit()  # Cities are committed

    restaurants = [
        Restaurant(
            name='Lemoni Greek Cuzina',
            street_number='1795',
            street_name='Wynnum Rd',
            phone='0733905505',
            email='bookings@lemoni.com.au',
            cuisine='Greek',
            city_id=cities[0].id
        ),
        Restaurant(
            name='Pho Bistro & Grill',
            street_number='348',
            street_name='Bagot Rd',
            phone='(08) 8981 4914',
            email='phobistrodarwin@gmail.com',
            cuisine='Vietnamese',
            city_id=cities[3].id
        ),
        Restaurant(
            name='Stax Burger Co.',
            street_number='98',
            street_name='Prospect Rd',
            phone='(08) 8344 5873',
            email='hello@staxburger.com',
            cuisine='American',
            city_id=cities[4].id
        )
    ]

    db.session.query(Restaurant).delete()  # Delete any existing restaurant data first to avoid unexpected results
    db.session.add_all(restaurants)
    db.session.commit()  # Final commit to add restaurants to the database

    print("Models seeded")