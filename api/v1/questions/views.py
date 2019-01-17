
from flask import jsonify, request
from datetime import datetime
from . import questions_blueprint

from .models import Question
from ..meetups.models import Meetup

@questions_blueprint.route('/questions/',methods=['POST'])
def post_question():
    '''this endpoint submits a question for a meetup'''
    user = 1
    meetup = 1
    if user and meetup:
        data = {
            "created_by":user,
            "title":request.json["title"],
            "body":request.json["body"],
            "meetup":meetup,
        }
    else:
        return jsonify({
                        "status":404,
                        "error":"Question posting failed. User or Meetup not found."
                        }), 404
    question = Question().create_question(**data)
    if question:
        return jsonify({
                        "status":201,
                        "data":{
                            "user":user,
                            "meetup":meetup,
                            "title":question["title"],
                            "body":question["body"],
                        },
                    }), 200
    else:
        return jsonify({
                        "status":204,
                        "error":"Question posting failed"
                      }), 204

@questions_blueprint.route( '/questions/<int:question_id>', methods = ['GET'] )
def get_question(question_id):
    '''this endpoint gets a specific question'''
    question = Question.get_question(question_id)
    if question:
        return jsonify({"status":200,
                            "data":[{
                                "id":question["id"],
                                "title":question["title"],
                                "body":question["body"]
                            }]
                        }), 200  
    else:
        return jsonify({"status":404,
                        "error":"Question not Found"
                        }), 404

@questions_blueprint.route('/questions/', methods=['GET'])
def get_all_questions():
    '''this endpoint gets all the questions'''
    questions = Question.get_all_questions()

    if len(questions) > 1:
        return jsonify({"status":200,
                            "data":questions  
                        }), 200
    else:
        return jsonify({"status":404,
                            "error":"No questions found"  
                        }), 404


@questions_blueprint.route( '/questions/<int:question_id>/upvote', methods = ['PATCH'] )
def upvote_question(question_id):
    '''this endpoint submits an upvote for a specific question'''
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
    '''this endpoint submits a downvotes for a specific question'''
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