#meetups container list
from datetime import datetime
MEETUPS = [
    {
    "id":1,
    "created_on":datetime.now(),
	"topic":"Python!",
	"happening_on":"1/2/2019",
	"location":"iHub",
	"images":[],
	"tags":[{"tag_1":"tag one"},{"tag_2":"tag two"}]
},
{
    "id":2,
    "created_on":datetime.now(),
	"topic":"Ruby!",
	"happening_on":"1/2/2019",
	"location":"iHub",
	"images":[],
	"tags":[{"tag_1":"tag one"},{"tag_2":"tag two"}]
}
]

class Meetup(object):
    '''this class defines a blueprint of a meetup record'''
    # def __init__(self, *args, **kwargs):
    #     print("kwargs",kwargs)
    #     self.meetups = MEETUPS
    #     self.meetup = kwargs
    #     MEETUPS.append(self.meetup)

    def __repr__(self):
        return "<Meetup: {}>".format(self.title)

    @staticmethod
    def get_meetup(meetup_id):
        '''this function fetches on meetup record 
        and returns it or returns an error if it is not found
         '''
        meetups = MEETUPS
        
        meetup_ = [meetup for meetup in meetups if meetup["id"] == meetup_id]
        if len(meetup_)!= 0:
            return meetup_[0]
        else:
            return "error"
       