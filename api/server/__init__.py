from flask import Flask
from flask_restful_swagger_3 import Api

from .extensions import *
from .utils.helpers import generate_response
from .utils.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, \
    HTTP_405_METHOD_NOT_ALLOWED

app = Flask(__name__)
app.config.from_object("config.Config")
app.config.from_prefixed_env()

ma.init_app(app)
mongo.init_app(app)

# api
api = Api(app,  version="1.0")
api.prefix = '/api'

from .questions import QuestionResource, QuestionsListResource, QuestionAddResource
api.add_resource(QuestionAddResource, '/question')
api.add_resource(QuestionResource, '/question/<string:slug>')
api.add_resource(QuestionsListResource, '/questions')

@app.errorhandler(HTTP_404_NOT_FOUND)
def not_found(e):
    return generate_response(message=str(e), status=HTTP_404_NOT_FOUND)

@app.errorhandler(HTTP_405_METHOD_NOT_ALLOWED)
def method_not_allowed(e):
    return generate_response(message=str(e), status=HTTP_405_METHOD_NOT_ALLOWED)

@app.errorhandler(Exception)
def unhandled_exception(e):
    if app.debug:
        raise e
    return generate_response(message=str(e), status=e.code if hasattr(e, "code") else HTTP_500_INTERNAL_SERVER_ERROR)
