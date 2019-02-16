from datetime import datetime

QUESTIONS = []
COMMENTS = []

class Question(object):
    '''this class represents blueprint/manipulations of questions'''
    def __init__(self):
        self.count = len(QUESTIONS)
    
    def create_question(self,**kwargs):
        '''a function to create a question'''
        question = {
            "id":self.count+1,
            "created_on":datetime.now(),
            "body":kwargs["body"],
            "votes":0,
            "meetup":kwargs["meetup"],
            "created_by":kwargs["created_by"],
            "title":kwargs["title"]
        }
        QUESTIONS.append(question)
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

    def get_all_questions():
        ''' this fucntion gets all questions posted '''
        questions = QUESTIONS
        return questions