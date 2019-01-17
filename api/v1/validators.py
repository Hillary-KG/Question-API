import re

def validate_password(pswd):
    ''' password validation '''
    if re.match('[A-Za-z0-9@#$%^&+=]{6,}', pswd) is None:
        return False
    else:
        return True
def  validate_username(uname):
    '''username validation'''
    if re.match('^[a-zA-Z][-\w.]{0,22}([a-zA-Z\d]|(?<![-.])_)$', uname) is None:
        return False
    else:
        return True

def validate_names(mystr):
    '''validate a string contains [a-zA-_]'''
    if re.match('^[a-zA-Z]$',str(mystr)) is None:
        return False
    else:
        return True

def validate_phone(phone_no):
    '''validate user phone number'''
    if re.match('^\+(?:[0-9]?){6,14}[0-9]$',phone_no) is None:
        return False
    else:
        return True

def validate_text_input(text):
    '''validate text inputs'''
    if re.match('^\w+$',text) is None:
        return False
    else:
        return True