from flask import Blueprint

meetups_blueprint = Blueprint('meetups', __name__,url_prefix='/api/v1/'
                        )
rsvp_blueprint = Blueprint('rsvp',__name__, url_prefix='/api/v1/')

