from flask_restful_swagger_3 import Schema


class StepSchema(Schema):
    properties = {
        'Title': {
            'type': 'string'
        },
        'Description': {
            'type': 'string'
        },
        'ImageUrl': {
            'type': 'string',
            'nullable': True
        }
    }

class QuestionModel(Schema):
    properties = {
        'Question': {
            'type': 'string'
        },
        'Options': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        },
        'CorrectAnswer': {
            'type': 'string'
        },
        'Solution': {
            'type': 'string'
        },
        'ImageUrl': {
            'type': 'string',
            'nullable': True
        },
        'Steps': StepSchema.array()
    }
