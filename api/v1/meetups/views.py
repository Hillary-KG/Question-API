<<<<<<< HEAD
from flask import jsonify,request
from .models import Rsvp
=======
import re
from datetime import datetime
from flask import request, jsonify

from .models import Rsvp, Meetup
>>>>>>> b0cb43bd02c6f0b1cdc310284c7207fffae7939b
from . import rsvp_blueprint
from . import meetups_blueprint

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
    meetup = Meetup().create_meetup(**data)

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

<<<<<<< HEAD
=======
@meetups_blueprint.route('/meetups/upcoming/',methods=['GET'])
def get_all_meetups():
    '''a endpoint to fetch all meetup records'''
    meetups = Meetup().get_all_meetups()
    
    if len(meetups) != 0:
        return jsonify({"status":200, "data":meetups}),200
    else:
        return jsonify({"status":404,"error":"No meetups found"}),404
    
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

>>>>>>> b0cb43bd02c6f0b1cdc310284c7207fffae7939b
@rsvp_blueprint.route('/meetups/<int:meetup_id>/rsvps/',methods=['POST'])
def rsvp_for_meetup(meetup_id):
    print("ID I am here",meetup_id)
    meetup = Meetup.get_meetup(meetup_id)
    user = request.json["user"]
    if user and meetup:
        data = {
            "meetup":meetup,    
            "response":request.json["response"],
            "user":user
        }
        rsvp = Rsvp().rsvp_meetup(**data)
        if rsvp:
            return jsonify({
                            "status":201,
                            "data":data
                            }), 201
        else:
            return jsonify({
                        "status":204,
                        "error":"RSVP submission failed.No data submitted"
                        }), 204
    else:
        return jsonify({
                        "status":404,
                        "error":"User or Meetup Not Found"
                        }), 404
<<<<<<< HEAD
    
    
=======

>>>>>>> b0cb43bd02c6f0b1cdc310284c7207fffae7939b
