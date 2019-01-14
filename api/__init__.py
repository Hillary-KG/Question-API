import os

# from flask_api import FlaskAPI 
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

#imporing the configuration dictionary object from the instance module 
from instance.config import app_config

from .v1.meetups.views import meetups_blueprint
# from .v1.questions import questions_blueprint
# from .v1.users.blueprints import login_blueprint, signup_blueprint, home_blueprint, simple_page 
from .v1.users.views import simple_page, login_blueprint, signup_blueprint, home_blueprint
from .v1.questions.views import questions_blueprint

#initializinng sqlalchemy 
# db = SQLAlchemy()

def create_app(config_name):
    '''initializing/creating the flask app(object)'''
    app = Flask(__name__,instance_relative_config=True,template_folder='templates',static_folder='static')
    app.config.from_object(app_config[config_name])#using development app configurations
    app.config.from_pyfile("config.py")
    #registering the blueprints here 
    app.register_blueprint(simple_page)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(signup_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(meetups_blueprint)

    print("\nurls here\n\n\n",str(app.url_map))      
    return app