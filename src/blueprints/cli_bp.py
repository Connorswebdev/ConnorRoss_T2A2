from init import db, bcrypt
from models.user import User
from models.allergy import Allergy
from models.restaurant import Restaurant
from models.locations import Location
from models.city import City
from flask import Blueprint

cli_bp = Blueprint('db', __name__)

# This command creates the database table structures based on the imported models above
@cli_bp.cli.command("create")
def create_db():
    db.drop_all() # Any existing tables are first dropped to ensure a clean slate
    db.create_all()
    print("Tables created successfully") # A message is printed when the database tables are successfully created


# This command inputs data into the previously created tables
@cli_bp.cli.command("seed")
def seed_db():
    users = [
        User(
            first_name='admin',
            l_name='admin',
            email='admin@dineandwine.com',
            password=bcrypt.generate_password_hash('admin123%').decode('utf-8'),
            is_admin=True
        ),
        User(
            f_name='John',
            l_name='Doe',
            email='hello@fakeemail.com',
            password=bcrypt.generate_password_hash('Johndoe1!').decode('utf-8'),
            is_admin=False
        ),
        User(
            f_name='Robin',
            l_name='Banks',
            email='idonotrobbanks@mymail.com',
            password=bcrypt.generate_password_hash('iluvmoney!').decode('utf-8'),
            is_admin=False
        )
    ]

    db.session.query(User).delete() # Delete any existing User data first to avoid unexpected results
    db.session.add_all(users)
    db.session.commit() # Users are committed 

    # Only Australian locations are entered currently for demonstration purposes
locations = [
    Location(
        name='Melbourne'
    ),
    Location(
        name='Brisbane'
    ),
    Location(
        name='Hobart'
    ),
    Location(
        name='Adelaide'
    ),
    Location(
        name='Sydney'
    ),
    Location(
        name='Perth'
    )
]

db.session.query(Location).delete() # Delete any existing location data first to avoid unexpected results
db.session.add_all(locations)
db.session.commit() # locations are committed so it can be added to the cities model as a foreign key

    # Only select cities are added here for demonstration purposes
cities = [
        City(
            name='Tingalpa',
            postcode='4173',
            location_id=locations[0].id
        ),
        City(
            name='Mayfield',
            postcode='2304',
            location_id=locations[1].id
        ),
        City(
            name='Cocount Grove',
            postcode='0810',
            location_id=locations[3].id
        ),
        City(
            name='Riverton',
            postcode='6148',
            location_id=locations[4].id
        ),
        City(
            name='Prospect',
            postcode='5082',
            location_id=locations[2].id
        )
    ]

db.session.query(City).delete() # Delete any existing cities data first to avoid unexpected results
db.session.add_all(cities)
db.session.commit() # Cities are committed so it can be added to the venues model as a foreign key

restaurants = [
        Restaurant(
            name='Lemoni Greek Cuzina',
            street_number='59',
            street_name='Bundaleer St',
            phone='0733741360',
            email='hello@bundaleer.com',
            cost_per_head='190',
            min_guests='80',
            max_guests='200',
            city_id=cities[2].id
        ),
        Restaurant(
            name='Dalywaters Roses Garden and Chapel',
            street_number='240',
            street_name='Bungower Rd',
            phone='0425608264',
            email='hello@dalywaters.com',
            cost_per_head='220',
            min_guests='50',
            max_guests='150',
            city_id=cities[1].id
        ),
        Restaurant(
            name='Quamby Elocation',
            street_number='1145',
            street_name='Westwood Rd',
            phone='0412345678',
            email='hello@quambyelocation.com',
            cost_per_head='220',
            min_guests='80',
            max_guests='300',
            city_id=cities[4].id
        )
    ]

db.session.query(Venue).delete() # Delete any existing venue data first to avoid unexpected results
db.session.add_all(venues)
db.session.commit() # Venues are committed so it can be added to the weddings model as a foreign key

weddings = [
        Wedding(
            date_of_wedding='2023-11-30',
            user_id=users[0].id,
            venue_id=venues[1].id
        ),
        Wedding(
            date_of_wedding='2024-05-12',
            user_id=users[1].id,
            venue_id=venues[2].id
        ),
        Wedding(
            date_of_wedding='2025-01-02',
            user_id=users[2].id,
            venue_id=venues[0].id
        )
    ]

db.session.query(Wedding).delete() # Delete any existing wedding data first to avoid unexpected results
db.session.add_all(weddings)
db.session.commit() # Final commit to add weddings to the database

print("Models seeded")