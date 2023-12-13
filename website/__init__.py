import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Check if SQLALCHEMY_DATABASE_URI is set
    if not app.config.get('SQLALCHEMY_DATABASE_URI'):
        raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set. Please provide a valid URI.")

    db.init_app(app)
    migrate.init_app(app, db)

    from views import views
    from auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import User, Allergy, Restaurant

    return app
