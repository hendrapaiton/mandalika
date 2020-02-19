# Import from system libraries
from flask_mongoengine import MongoEngine

# MongoEngine load to db variable
db = MongoEngine()


# Function to initialize db to app
def initialize_db(app):
    db.init_app(app)
