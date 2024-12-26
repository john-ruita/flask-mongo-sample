from flask import Flask, render_template
from flask_restful import Api

from .extensions import *
from .utils.helpers import generate_response
from .utils.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_405_METHOD_NOT_ALLOWED

# Initialize Flask application
app = Flask(__name__)

# Load configuration from object and environment variables
app.config.from_object("config.Config")
app.config.from_prefixed_env()

# Initialize extensions
ma.init_app(app)
mongo.init_app(app)

# Define route for the index page
@app.route("/")
def index():
    return render_template("index.html")

# Initialize Flask-RESTful API
api = Api(app)
api.prefix = '/api'

# Import and add resources to the API
from .questions import QuestionResource, QuestionsListResource
api.add_resource(QuestionResource, '/question', '/question/<string:slug>')
api.add_resource(QuestionsListResource, '/questions')

# Error handler for 404 Not Found
@app.errorhandler(HTTP_404_NOT_FOUND)
def not_found(e):
    return generate_response(message=str(e), status=HTTP_404_NOT_FOUND)

# Error handler for 405 Method Not Allowed
@app.errorhandler(HTTP_405_METHOD_NOT_ALLOWED)
def method_not_allowed(e):
    return generate_response(message=str(e), status=HTTP_405_METHOD_NOT_ALLOWED)

# General error handler for unhandled exceptions
@app.errorhandler(Exception)
def unhandled_exception(e):
    if app.debug:
        raise e
    return generate_response(message=str(e), status=e.code if hasattr(e, "code") else HTTP_500_INTERNAL_SERVER_ERROR)
