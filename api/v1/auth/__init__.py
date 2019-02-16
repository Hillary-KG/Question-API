from flask import Blueprint

signup_blueprint = Blueprint( 'signup', __name__, url_prefix = '/api/v1/auth/' )
login_blueprint = Blueprint( 'login', __name__, url_prefix = '/api/v1/auth/' )
pswd_reset_blueprint = Blueprint( 'pswd_reset', __name__, url_prefix = '/api/v1/auth/' )