from flask import make_response, request
from flask_restful import Resource

from .services import *


class QuestionResource(Resource):
    """
    Resource for handling individual question operations.

    Methods:
        get(slug): Retrieve a question by its slug.
        post(): Insert a new question.
        put(slug): Update an existing question by its slug.
        delete(slug): Delete a question by its slug.
    """
    @staticmethod
    def get(slug):
        return make_response(retrieve_question(slug))

    @staticmethod
    def post():
        return make_response(post_question(request.get_json()))

    @staticmethod
    def put(slug):
        return make_response(update_question(slug, request.get_json()))

    @staticmethod
    def delete(slug):
        return make_response(delete_question(slug))


class QuestionsListResource(Resource):
    """
    Resource for handling operations on the list of questions.

    Methods:
        get(): Retrieve a paginated list of questions.
    """
    @staticmethod
    def get():
        return make_response(list_questions())
