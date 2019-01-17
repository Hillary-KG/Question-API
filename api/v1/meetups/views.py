import re
from datetime import datetime
from flask import request, jsonify

from .models import Rsvp, Meetup
from . import rsvp_blueprint
from . import meetups_blueprint

@meetups_blueprint.route('/meetups/<int:meetup_id>',methods=['GET'])
def get_meetup(meetup_id):
    meetup = Meetup.get_meetup(meetup_id)
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

@meetups_blueprint.route('/meetups/',methods=['POST'])
def create_meetup():
    '''a endpoint to create a meetup record'''
    data = {
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
    meetup = Meetup().create_meetup(**data)

    if meetup:
        print("meetup id",meetup["id"])
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

@meetups_blueprint.route('/meetups/upcoming/',methods=['GET'])
def get_all_meetups():
    '''a endpoint to fetch all meetup records'''
    meetups = Meetup.get_all_meetups()
    
    if len(meetups) != 0:
        return jsonify({"status":200, "data":meetups}),200
    else:
        return jsonify({"status":404,"error":"No meetups found"}),404

@rsvp_blueprint.route('/meetups/<int:meetup_id>/rsvps/',methods=['POST'])
def rsvp_for_meetup(meetup_id):
    meetup = Meetup.get_meetup(meetup_id)
    user = request.json["user"]
    if user and meetup != "error":
        data = {
            "meetup":meetup["id"],
            "topic":meetup["topic"],
            "status":request.json["response"],
        }
        return jsonify({
                        "status":201,
                        "data":data
                        }), 201
    else:
        return jsonify({
                        "status":404,
                        "data":"User or Meetup Not Found"
                        }), 404

