from flask import Flask, request
from flask_restful import Api

from .extensions import *
from .utils.helpers import generate_response
from .utils.http_codes import HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND

app = Flask(__name__)
app.config.from_object("config.Config")
app.config.from_prefixed_env()

ma.init_app(app)
mongo.init_app(app)

# api
api = Api(app)
api.prefix = '/api'

# exception handlers
@app.errorhandler(HTTP_401_UNAUTHORIZED)
def unauthorized(e):
    return generate_response(message=str(e), status=HTTP_401_UNAUTHORIZED)

@app.errorhandler(HTTP_404_NOT_FOUND)
def not_found(e):
        return generate_response(message=f"{str(e)} {request.path}", status=HTTP_404_NOT_FOUND)
