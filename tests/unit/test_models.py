# Project Modules
from server.db.work_with_db import DatabaseConnection


def test_db_connection():
    """
    GIVEN a new database connection
    WHEN a new connection is created
    THEN check the connection is established
    """
    connection = DatabaseConnection()

    assert connection is not None
