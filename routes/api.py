# Import from application modules
from routes.Login import LoginApi
from routes.User import User2Api, UserApi


# Function to initialize route to API Flask
def initialize_routes(api):
    api.add_resource(LoginApi, '/api/v1/login')
    api.add_resource(User2Api, '/api/v1/user')
    api.add_resource(UserApi, '/api/v1/user/<id>')
