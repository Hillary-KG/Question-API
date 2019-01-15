import re
from datetime import datetime
import json
from flask import request, jsonify


from . import meetups_blueprint
from .models import Meetup

@meetups_blueprint.route('/meetups/',methods=['POST'])
def create_meetup():
    '''a endpoint to create a meetup record'''
    meetup = {
        "id":request.json['id'],
        "topic":request.json['topic'],
        "created_on":datetime.now(),
        "happening_on":request.json['happening_on'],
        "location":request.json['location'],
        "images":request.json['images'],
        "tags":request.json['tags']
    }
    
    #validation
    if re.match('.*[a-zA-Z0-9]+.*', meetup["topic"]) is None:
        return jsonify({'response': 'invalid topic'}), 400
    
    meetup = Meetup().create_meetup(**meetup)

    if meetup:
        return jsonify({
                        "status":201,
                        "data":meetup
                        }),201
    else:
        return jsonify({"status":204,
                        "error":"Meetup creation failed"
                        }),204