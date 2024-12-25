from flask import make_response, request
from flask_restful_swagger_3 import Resource, swagger

from .schema import QuestionModel
from .services import *


class QuestionResource(Resource):
    @swagger.tags('Question')
    @swagger.reorder_with(QuestionModel, description="Returns a Question", summary="Get a Question")
    def get(self, slug):
        return make_response(retrieve_question(slug))

    @swagger.tags('Question')
    @swagger.reorder_with(QuestionModel, description="Returns a Question", summary="Update a Question")
    def put(self, slug):
        return make_response(update_question(slug, request.get_json()))

    @swagger.tags('Question')
    @swagger.reorder_with(QuestionModel, description="Returns a Question", summary="Delete a Question")
    def delete(self, slug):
        return make_response(delete_question(slug))

class QuestionAddResource(Resource):
    @swagger.tags('Question')
    @swagger.reorder_with(QuestionModel, description="Returns a Question", summary="Create a Question")
    def post(self):
        return make_response(post_question(request.get_json()))


class QuestionsListResource(Resource):
    @swagger.tags('Question')
    @swagger.reorder_with(QuestionModel, description="Returns a list of Questions", summary="Get Questions")
    def get(self):
        return make_response(list_questions())
