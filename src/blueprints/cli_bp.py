from init import db, bcrypt
from models.user import User
from models.allergy import Allergy
from models.restaurant import Restaurant
from models.locations import Location
from models.city import City
from flask import Blueprint

# cli_bp = Blueprint('db', __name__)

# This command creates the database table structures based on the imported models above
@cli_bp.cli.command("create")
def create_db():
    with app.app_context():
        db.drop_all()  # Any existing tables are first dropped to ensure a clean slate
        db.create_all()
        print("Tables created successfully")  # A message is printed when the database tables are successfully created


# This command inputs data into the previously created tables
@cli_bp.cli.command("seed")
def seed_db():
    with app.app_context():
        users = [
            User(
                first_name='admin',
                last_name='admin',
                email='admin@dineandwine.com',
                password=bcrypt.generate_password_hash('admin123%').decode('utf-8'),
                is_admin=True
            ),
            User(
                first_name='John',
                last_name='Doe',
                email='hello@fakeemail.com',
                password=bcrypt.generate_password_hash('Johndoe1!').decode('utf-8'),
                is_admin=False
            ),
            User(
                first_name='Robin',
                last_name='Banks',
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
    db.session.commit() # Cities are committed 
    restaurants = [
            Restaurant(
                name='Lemoni Greek Cuzina',
                street_number='1795',
                street_name='Wynnum Rd',
                phone='0733905505',
                email='bookings@lemoni.com.au',
                cuisine = 'Greek',
                city_id=cities[0].id
            ),
            Restaurant(
                name='Pho Bistro & Grill',
                street_number='348',
                street_name='Bagot Rd',
                phone='(08) 8981 4914',
                email='phobistrodarwin@gmail.com',
                cuisine = 'Vietnamese',
                city_id=cities[3].id
            ),
            Restaurant(
                name='Stax Burger Co.',
                street_number='98',
                street_name='Prospect Rd',
                phone='(08) 8344 5873',
                email='hello@staxburger.com',
                cuisine = 'American',
                city_id=cities[2].id
            )
        ]

    print("Models seeded")