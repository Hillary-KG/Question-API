import re
from datetime import datetime
from flask.views import View, MethodView
import json
from flask import request, jsonify, Blueprint, Flask


from . import meetups_blueprint
from .models import Meetup

@meetups_blueprint.route('/meetups/',methods=['POST'])
def create_meetup():
    '''a endpoint to create a meetup record'''
    meetup = {
        "id":request.json['id'],
        "topic":request.json['topic'],
        "created_on":datetime.now(),
        "happening_on":request.json['venue'],
        "images":request.json['images'],
        "tags":request.json['tags']
    }
    
    #validation
    if re.match('.*[a-zA-Z0-9]+.*', meetup["topic"]) is None:
        return jsonify({'response': 'invalid topic'}), 400
    # if re.match('.*[a-zA-Z0-9]+.*',venue):
    #     return jsonify({'response':'invalid venue entry'})
    _meetup = Meetup(**meetup)

    if _meetup.topic:
        return jsonify({'response':'meetup created successfully'}),201
    else:
        return jsonify({'response':'meetup creation failed'}),40