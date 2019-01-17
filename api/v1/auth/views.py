from flask import request, jsonify
from validate_email import validate_email
from werkzeug.security import check_password_hash


from . import signup_blueprint, login_blueprint, pswd_reset_blueprint
from ..validators import validate_names, validate_username, validate_password, validate_phone
from .models import User, Token


@signup_blueprint.route('/register/', methods = ['POST'])
def register_user():
    '''registering new user'''
    data = {
            "first_name":request.json["first_name"],
            "last_name":request.json["last_name"],
            "other_name":request.json["other_name"],
            "phone_number":request.json["phone_number"],
            "user_name":request.json["user_name"],
            "email":request.json["email"],
            "is_admin":request.json["is_admin"],
            "password":request.json["password"],
            "confirm_pswd":request.json["confirm_password"],
        }
    try:
        if ((validate_names(data["first_name"]==False))) and (validate_names(data["last_name"]==False)) \
                and (validate_names(data["other_name"])==False):
            return jsonify({"status":100,
                    "error": "Invalid names. Names can only have characters"
            }), 400

        if not validate_email(data["email"]):
            return jsonify({
                "status": 400,
                "error": "Not a valid email"
            }), 400
        
        if (validate_username(data["user_name"]) == False):
            return jsonify({
                "status": 400,
                "error": "Please enter a valid user name"
            }), 400

        if (validate_phone(data["phone_number"])==False):
            return jsonify({
                "status": 400,
                "error": "Please enter a valid phone number"
            }), 400

        if (validate_password(data["password"])==False):
            return jsonify({
                "status": 400,
                "error": "password not valid. Must be at least characters long, aphanumeric \
                            and have atleast on special character"
            }), 400

        if ( data["password"].replace(" ","") != data["confirm_pswd"].replace(" ","") ):
            return jsonify({
                "status": 400,
                "error": "passwords did not match!"
            }), 400

        #create user
        user = User().create_user(**data)

        if user:
            return jsonify({
                "status": 201,
                "data": user
            }), 201
        else:
            return jsonify({
                "status": 302,
                "error": "user exists"
            }), 302
    except Exception as e:
        print("Invalid name input", e)
        return jsonify({
            "status": 500,
            "error":"something went wrong, please try again."
        }), 500

@login_blueprint.route('/login/', methods = ['POST'])
def login():
    '''login user'''
    username = request.json["username"]
    pswd = request.json["password"].replace(" ","")
    try:
        user = User().check_if_exists(username)
        if user:
            if check_password_hash(user["password"], pswd):
                auth_token = Token(user["id"]).token
                
                Token.save_token(auth_token)
                if auth_token:
                    return jsonify({
                        "status": 200,
                        "token": auth_token.decode(),
                    }), 200
                else:
                    return jsonify({
                        "status": 401,
                        "error": "user authentication failed"
                    }), 401
    except Exception as e:
        print("User login failed", e)
        return jsonify({
            "status": 404,
            "error": "user not found"
        })

@pswd_reset_blueprint.route('/resetPassword/', methods = ['PATCH'])
def reset_password():
    pass


