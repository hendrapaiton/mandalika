# Import from system libraries
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api

# Import from application modules
from errors import errors
from models.User import User
from models.db import initialize_db
from routes.api import initialize_routes

# Flask app instance with static (html, css and js) folder configuration
app = Flask(__name__)
# Flask Restful configuration with errors included
api = Api(app, errors=errors)
# Files for Configuration System in environment
app.config.from_envvar('ENV_FILE_LOCATION')
# BCrypt instances
bcrypt = Bcrypt(app)
# JWT instances
jwt = JWTManager(app)


# Get roles for authenticated user
@jwt.user_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}


# Load user identity
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


# Database Configuration Initialization
initialize_db(app)
# API (Routing) Configuration Initialization
initialize_routes(api)

# Admin account initialization for first uses
user = User.objects(username='admin@nj.net')
if not user:
    login = User(username='admin@nj.net', password='enje123', roles=['admin'])
    login.hash_password()
    login.save()

# Running Flask Application when main class executed
if __name__ == '__main__':
    app.run()
