from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class='website.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from website.models import User, Allergy, Restaurant

    return app
