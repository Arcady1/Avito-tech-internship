# Built-in modules
from uuid import uuid4


def id_generator():
    """
    The function generates a unique id.

    :return: str. Unique id
    """
    return str(uuid4())


def modify_response(response: dict, status: int, message: str = "", error=""):
    """
    The function modifies a response.

    :param response: dict. A link to response dict.
    :param status: int. A response status code.
    :param message: str. A response message.
    :param error: Error. An error
    """
    response["status"] = status
    response["message"] = message
    if error:
        response["description"] = str(error)
