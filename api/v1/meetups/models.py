
from datetime import datetime
from flask import jsonify

MEETUPS = []


class Meetup(object):
    '''this class defines a blueprint of a meetup record'''
    def __init__(self, *args, **kwargs):
        self.meetups = MEETUPS
        self.meetup = kwargs
        MEETUPS.append(self.meetup)

    def __repr__(self):
        return "<Meetup: {}>".format(self.title)

    @staticmethod
    def get_all_meetups():
        meetups = MEETUPS
        '''function to get all the meetups'''
        return meetups