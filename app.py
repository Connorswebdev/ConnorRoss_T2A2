from flask import Flask
from init import db, ma, bcrypt, jwt
from flask_migrate import Migrate
from marshmallow.exceptions import ValidationError
from dotenv import load_dotenv 
import os

# Load environment variables from .env file
load_dotenv()

# Create instances of the extensions without attaching to the app for now
db_instance = db
ma_instance = ma
bcrypt_instance = bcrypt
jwt_instance = jwt

# App main function that notifies Flask where all functionalities are located
def create_app():

    # Initialize app
    app = Flask(__name__)

    # Load secrets from .env file, 
    # including URI to connect to the database which contains the password,
    # and JWT key used for encryption
    load_dotenv()
    URI = os.environ.get('URI')
    SECRET_JWT_KEY = os.environ.get('SECRET_JWT_KEY')

    # Set database URI
    app.config["SQLALCHEMY_DATABASE_URI"] = URI

    # Set JWT key
    app.config["JWT_SECRET_KEY"] = SECRET_JWT_KEY

    # Attach initialized extensions to the app
    db.init_app(app)
    ma_instance.init_app(app)
    jwt_instance.init_app(app)
    bcrypt_instance.init_app(app)

    # The following error handlers capture errors that may occur in this app
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
    
    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.__dict__['messages']}, 400
    
    # Blueprint imports are here to remove a circular import
    from src.blueprints.cli_bp import cli_bp
    from src.blueprints.auth_bp import auth_bp
    from src.blueprints.users_bp import users_bp
    from src.blueprints.restaurant_bp import restaurants_bp
    from src.blueprints.allergy_bp import allergy_bp

    # Registering blueprints to run with the command "flask run"
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp, name='users_bp')
    app.register_blueprint(allergy_bp)
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(users_bp)

    return app

# This block checks if the script is being run directly
if __name__ == '__main__':
    app = create_app()
    migrate = Migrate(app, db)  
    with app.app_context():
        migrate.init_app(app)
        app.run()