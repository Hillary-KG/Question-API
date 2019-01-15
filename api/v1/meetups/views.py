import re
from datetime import datetime
import json
from flask import request, jsonify


from . import meetups_blueprint
from .models import Meetup

@meetups_blueprint.route('/meetups/<int:meetup_id>',methods=['GET'])
def get_meetup(meetup_id):
    meetup = Meetup().get_meetup(meetup_id)
    if meetup != "error":
        return jsonify({"status":200,
                         "data":[{
                            "id":meetup["id"],
                            "topic":meetup["topic"],
                            "location":meetup["location"],
                            "happening_on":meetup["happening_on"],
                            "tags":meetup["tags"],
                }]
            }), 200
    else:
        return jsonify({"status":404,
                        "error":"Meetup NOT found",
                        }), 404