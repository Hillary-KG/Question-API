from flask import jsonify,request
from .models import Rsvp, Meetup
from . import rsvp_blueprint

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
    
    