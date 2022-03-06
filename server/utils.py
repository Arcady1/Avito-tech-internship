# Built-in modules
from uuid import uuid4


def id_generator():
    """
    The function generates a unique id.

    :return: str. Unique id
    """
    return str(uuid4())
