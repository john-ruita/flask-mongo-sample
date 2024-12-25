from functools import wraps

from flask import request

from ..utils.http_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY


def generate_response(data=None, message=None, status=HTTP_200_OK, **kwargs):
    """
    It takes in a data, message, and status, and returns a dictionary with the data, message, and status

    :param data: The data that you want to send back to the sacco
    :param message: This is the message that you want to display to the user
    :param status: The HTTP status code, defaults to 400 (optional)
    :return: A dictionary with the keys: data, message, status.
    """

    response = {
        "message": "Validation Error" if status == HTTP_422_UNPROCESSABLE_ENTITY else message,
        **kwargs
    }
    if status == HTTP_200_OK or status == HTTP_201_CREATED:
        response["data"] = data
    elif status == HTTP_422_UNPROCESSABLE_ENTITY:
        response["errors"] = data
    return response, status


"""Decorator that adds pagination to a function that returns a list of items"""
def paginate(f, arg_keys={'page': 1, 'per_page': 10}):
    @wraps(f)
    def decorated(*args, **kwargs):
        entries = {key: int(request.args.get(key, value)) for key, value in arg_keys.items()}
        return f(*args, **entries, **kwargs)
    return decorated
