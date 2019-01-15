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
    data = {
        "id":request.json['id'],
        "topic":request.json['topic'],
        "created_on":datetime.now(),
        "happening_on":request.json['happening_on'],
        "location":request.json['location'],
        "images":request.json['images'],
        "tags":request.json['tags']
    }

     #validation
    if re.match('.*[a-zA-Z0-9]+.*', data["topic"]) is None:
        return jsonify({'response': 'invalid topic'}), 400
    meetup = Meetup(**data).meetup

    if meetup:
        return jsonify({"status":201,
                        "data":[{
                            "topic":meetup["topic"],
                            "created_on":meetup["created_on"],
                            "happening_on":meetup["happening_on"],
                            "location":meetup["location"],
                            "tags":meetup["tags"]
                            }]
                        }),201
    else:
        return jsonify({'status':400,"error":'meetup creation failed'}), 400

@meetups_blueprint.route('/meetups/',methods=['GET'])
def get_all_meetups():
    '''a endpoint to fetch all meetup records'''
    meetups = Meetup().get_all_meetups()
    
    if len(meetups) != 0:
        return jsonify({"status":200, "data":meetups}),200
    else:
        return jsonify({"status":404,"error":"No meetups found"}),404

