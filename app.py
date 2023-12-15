from flask import Flask
from init import db, ma, bcrypt, jwt
from flask_migrate import Migrate
from marshmallow.exceptions import ValidationError
from os import environ
from dotenv import load_dotenv  # Add this line

# Load environment variables from .env file
load_dotenv()

#App main function that notifies Flask where all functionalities are located
def setup():
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.json.sort_keys = False

    # Imports from init used to initialize the application
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # The following error handlers capture errors that may occur in this app and returns an error message in a user friendly format
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

    # Registering blueprints to run with command "flask run"
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(allergy_bp)
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(users_bp)

    return app
if __name__ == "__main__":
    app = setup()
    app.run(debug=True)