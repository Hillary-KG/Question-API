import uuid
from datetime import datetime
from flask import jsonify

MEETUPS = []

class Meetup(object):
    '''this class defines a blueprint of a meetup record'''
    def __repr__(self):
        return "<Meetup: {}>".format(self.title)
    
    def create_meetup(self,**kwargs):
        '''this function creates a meetup record in the api'''
        MEETUPS.append(kwargs)
        return kwargs

    
