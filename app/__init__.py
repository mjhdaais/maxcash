from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from celery import Celery

from config import app_config
import celeryconfig

db = SQLAlchemy()
login_manager = LoginManager()

celery = Celery(__name__, 
	        broker='amqp://',
            backend='redis://',
            include=['app.tasks'])

celery.config_from_object(celeryconfig)

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(app_config[config_name])
	db.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = 'auth.sign_in'
	migrate = Migrate(app, db)

	from app import models

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .dashboard import dash as dash_blueprint
	app.register_blueprint(dash_blueprint)

	return app	