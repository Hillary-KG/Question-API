from flask import Blueprint

rsvp_blueprint = Blueprint('rsvp', __name__, url_prefix='/api/v1/')
meetups_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1/')

