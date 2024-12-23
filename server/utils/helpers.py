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

    return {
        "data" if status == HTTP_200_OK or status == HTTP_201_CREATED else "errors": data,
        "message": "Validation Error" if status == HTTP_422_UNPROCESSABLE_ENTITY else message,
        **kwargs
    }, status