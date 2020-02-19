import datetime

# Import from system libraries
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from mongoengine import DoesNotExist

# Import from application modules
from errors import UnauthorizedError, InternalServerError
from models.User import User


# Class Login API to load in Routes
class LoginApi(Resource):
    # Function to Login with HTTP POST Method
    def post(self):
        try:
            # get body (json) from client request
            body = request.get_json()
            # get user object from database with condition username from request
            user = User.objects.get(username=body.get('username'))
            # check password (encryption)
            authorized = user.check_password_hash(body.get('password'))
            # if check password (decryption) failed raise Error with code UnauthorizedError
            if not authorized:
                raise UnauthorizedError
            # giving expire times for login
            expires = datetime.timedelta(days=1)
            # create access token with utility from flask-jwt-extended
            access_token = create_access_token(identity=user, expires_delta=expires)
            # response client with token and status code
            return {'token': access_token}, 200
        # if request failed or does not meet specifications
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
