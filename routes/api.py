# Import from system libraries
from routes.Login import LoginApi


# Function to initialize route to API Flask
def initialize_routes(api):
    api.add_resource(LoginApi, '/api/v1/login')
