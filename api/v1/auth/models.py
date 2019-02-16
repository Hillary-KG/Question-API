from datetime import datetime, timedelta
import jwt 
from instance.config import Config
from werkzeug.security import generate_password_hash


#users contsiner list(DB)
USERS = []
#auth tokens container
AUTH_TOKENS = []

class User(object):
    def __init__(self):
        '''initializing instance variables here'''
        self.count = len(USERS)
        self.users = USERS
   
    def create_user(self, **kwargs):
        user = {
            "id":self.count + 1,
            "first_name":kwargs["first_name"],
            "last_name":kwargs["last_name"],
            "other_name":kwargs["other_name"],
            "phone_number":kwargs["phone_number"],
            "user_name":kwargs["user_name"],
            "email":kwargs["email"],
            "registered":datetime.now(),
            "is_admin":kwargs["is_admin"],
            "password":generate_password_hash(kwargs["password"].replace(" ","")),
            "confirm_pswd":generate_password_hash(kwargs["confirm_pswd"].replace(" ","")),
        }

        if self.check_if_exists(user["user_name"]):
            return None
        else:
            self.users.append(user)
            return user

        
        

    def get_user(self, user_id):
        '''this function gets a specific user'''
        users_ = [user for user in self.users if user["id"] == user_id]
        if len(users_) > 1:
            user = users_[0]
            return user
        else:
            return None

    def delete_user(self, user_id):
        '''this fucntions deletes a user from the users records'''
        item = self.user.pop(user_id - 1)
        return item

    def check_if_exists(self,user_name):
        '''checks if user exists'''
        for i in self.users:
            if ( i["user_name"] == user_name ):
                return i
            else:
                return None


class Token(object):
    def __init__(self,user_id):
        '''generating token for user authentication '''
        self.tokens = AUTH_TOKENS
        payload = {
            'sub':user_id,
            'exp':datetime.now() + timedelta ( minutes=30 ),
            'iat':datetime.now(),
        }
        self.token =  jwt.encode(payload, Config.SECRET)

    @staticmethod
    def decode_token(token):
        '''decoding user auth token to get the user id'''
        try:
            payload = jwt.decode(token, Config.SECRET)
            return payload["sub"]
        except Exception as e:
            print("Token error", e)
            return None

    @staticmethod
    def save_token(token):
        '''saving the generated token'''
        try:
            AUTH_TOKENS.append(token)
            return True
        except Exception as e:
            print("token storage error", e)
            return False
            
        
