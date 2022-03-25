# Project Modules
from server.db.work_with_db import DatabaseConnection


def test_db_connection_success(test_client):
    """
    GIVEN a new database connection
    WHEN a new connection is created
    THEN check the connection is established
    """
    with DatabaseConnection() as cursor:
        assert cursor is not None


def test_db_connection_error(test_client):
    """
    GIVEN a new database connection
    WHEN a new connection is not created
    THEN check the connection status
    """
    config = {
        "host": "localhost",
        "user": "wrong",
        "password": 123,
        "database": "test",
        "port": 8000
    }
    with DatabaseConnection(connection_conf=config) as cursor:
        assert cursor is None
