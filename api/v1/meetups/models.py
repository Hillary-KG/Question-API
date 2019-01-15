MEETUPS = []

RSVPS = []

class Meetup(object):
    '''this class defines a blueprint of a meetup record'''
    def __repr__(self):
        return "<Meetup: {}>".format(self.title)
    
    def create_meetup(self,**kwargs):
        '''this function creates a meetup record in the api'''
        MEETUPS.append(kwargs)
        return kwargs
      

class Rsvp(object):
    def rsvp_meetup(**kwargs):
        '''this function allow user to RSVP for a meetup'''
        rsvp = {
            "id":kwargs["id"],
            "meetup":kwargs["meetup"],
            "user":kwargs["user"],
            "response":kwargs["response"]
        }
        return rsvp
    def get_rsvp(id):
        '''this function gets a single rsvp record '''
        rsvps = RSVPS
        rsvp = [r for r in rsvps if r["id"]==id]
        if len(rsvp) > 0:
            return rsvp[0]
        else:
            return "error"
