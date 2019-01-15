import uuid
import urllib
from datetime import  datetime

QUESTIONS = []
COMMENTS = []

class Question(object):
    '''this class represents blueprint/manipulations of questions'''
    
    def create_question(self,**kwargs):
        '''a function to create a question'''
        question = {
            "id":kwargs["id"],
            "created_on":kwargs["created_on"],
            "body":kwargs["body"],
            "votes":kwargs["votes"],
            "meetup":kwargs["meetup"],
            "created_by":kwargs["created_by"],
            "title":kwargs["title"]
        }

        QUESTIONS.append(question)
        print("Questions", QUESTIONS)
        return question
    @staticmethod
    def get_question(question_id):
        '''function to fetch a specific question given the id'''
        questions = QUESTIONS
        question = [q for q in questions if q["id"]==question_id]
        print("question",len(question))
        if len(question) > 0:
            return question[0]
        else:
            return "error"
    # def get_all_questions(self,meetup_id):
    #     '''a func to get all questions of a meetup'''

    #     return [q for q in self.questions if q["meetup"]==meetup_id]

    # def upvote_question(self,question_id):
    #     '''a function to upvote a question'''
    #     question = self.get_question(question_id)
    #     question["upvotes"] += 1

    #     return question

    # def downvote_question(self,question_id):
    #     ''' a function to downvote a question '''
    #     question = self.get_question(question_id)
    #     question["downvotes"] += 1

    #     return question
