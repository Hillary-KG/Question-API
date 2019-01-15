
from flask import jsonify, request
from datetime import datetime
from . import questions_blueprint

from .models import Question

@questions_blueprint.route('/questions/',methods=['POST'])
def post_question():
    data = {
        "id":request.json["id"],
        "created_on":request.json["created_on"],
        "created_by":request.json["created_by"],
        "title":request.json["title"],
        "body":request.json["body"],
        "meetup":request.json["meetup"],
        "votes":request.json["votes"]
    }
    question = Question().create_question(**data)

    if question:
        return jsonify({
                        "status":201,
                        "data":question,
                        }),200
    else:
        return jsonify({
                        "status":204,
                        "error":"Question posting failed"
                        }),204

@questions_blueprint.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvote_question(question_id):
    question = Question().get_question(question_id)
    if question != "error":
        question["votes"] += 1
        return jsonify({"status":201,
                        "data":[{
                            "meetup":question["meetup"],
                            "title":question["title"],
                            "body":question["body"],
                            "votes":question["votes"]
                            }]
                        }), 201
    else:
        return jsonify({
                            "status":403,
                            "error":"Voting failed"
                        }), 403


@questions_blueprint.route('/questions/<int:question_id>/downvote', methods=['PATCH'])
def downvote_question(question_id):
    question = Question().get_question(question_id)
    if question != "error":
        question["votes"] -= 1
        return jsonify({"status":201,
                        "data":[{
                            "meetup":question["meetup"],
                            "title":question["title"],
                            "body":question["body"],
                            "votes":question["votes"]
                            }]
                        }), 201
    else:
        return jsonify({
                            "status":403,
                            "error":"Voting failed"
                        }), 403