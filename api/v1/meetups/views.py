from flask import jsonify,request
from .models import Rsvp, Meetup
from . import rsvp_blueprint

@rsvp_blueprint.route('meetups/<int:meetup_id>/rsvps/',methods=['POST'])
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


    