import re
from flask import jsonify,request

from .models import Rsvp, Meetup
from . import rsvp_blueprint
from . import meetups_blueprint

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

@rsvp_blueprint.route('/<int:meetup_id>/rsvps/',methods=['POST'])
def rsvp_for_meetup(meetup_id):
    print("ID I am here",meetup_id)
    meetup = Meetup.get_meetup(meetup_id)
    user = request.json["user"]
    if user and meetup:
        data = {
            "id":request.json["id"],
            "meetup":meetup,    
            "response":request.json["response"],
            "user":user
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
      
      
      