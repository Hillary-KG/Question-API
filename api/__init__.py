from flask import Flask

#imporing the configuration dictionary object from the instance module 
from instance.config import app_config

from .v1.meetups.views import meetups_blueprint
from .v1.questions.views import questions_blueprint
from .v1.meetups.views import rsvp_blueprint

def create_app(config_name):
    '''initializing/creating the flask app(object)'''
    app = Flask(__name__,instance_relative_config=True,template_folder='templates',static_folder='static')
    app.config.from_object(app_config[config_name])#using development app configurations
    app.config.from_pyfile("config.py")

    #registering the blueprints here 
    app.register_blueprint(meetups_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(rsvp_blueprint)

    print("\nurls here\n\n\n",str(app.url_map))
    
    return app