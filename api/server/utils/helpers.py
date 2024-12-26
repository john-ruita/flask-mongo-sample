from functools import wraps

from flask import request

from ..utils.http_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY


def generate_response(data=None, message=None, status=HTTP_200_OK, **kwargs):
    """
    Generate a standardized response for the API.

    Args:
        data (dict, optional): The data to include in the response. Defaults to None.
        message (str, optional): The message to include in the response. Defaults to None.
        status (int, optional): The HTTP status code for the response. Defaults to HTTP_200_OK.
        **kwargs: Additional keyword arguments to include in the response.

    Returns:
        tuple: A tuple containing the response dictionary and the HTTP status code.
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


def paginate(f, arg_keys={'page': 1, 'per_page': 10}):
    """
    A decorator to add pagination to a Flask route.

    Args:
        f (function): The function to be decorated.
        arg_keys (dict): A dictionary with default pagination arguments.

    Returns:
        function: The decorated function with pagination.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        entries = {key: int(request.args.get(key, value)) for key, value in arg_keys.items()}
        return f(*args, **entries, **kwargs)
    return decorated
