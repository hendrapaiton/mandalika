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
app = Flask(__name__, static_url_path='', static_folder='./static')
# Flask Restful configuration with errors included
api = Api(app, errors=errors)
# Files for Configuration System in environment
app.config.from_envvar('ENV_FILE_LOCATION')
# BCrypt instances
bcrypt = Bcrypt(app)
# JWT instances
jwt = JWTManager(app)

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


# Route for index file which index.html rendered from static folder
@app.route('/')
def index():
    return app.send_static_file('index.html')


# Running Flask Application when main class executed
if __name__ == '__main__':
    app.run()
