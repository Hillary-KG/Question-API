from flask import Blueprint

questions_blueprint = Blueprint(
                        'questions',
                        __name__,
                        url_prefix='/api/v1/'
                        )