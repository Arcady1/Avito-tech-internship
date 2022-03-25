# Built-in Modules
from string import Template

# Third Party Modules
import pymysql
from flask import current_app
from pymysql.constants import CLIENT


class DatabaseConnection:
    """ The class initializes database connections. """

    def __init__(self, connection_conf=None):
        self.connection = None
        self.cursor = None
        self.conn_conf = connection_conf

    def __enter__(self):
        try:
            if self.conn_conf is None:
                self.conn_conf = {
                    "host": current_app.config["MYSQL_LOCAL_HOST"],
                    "user": current_app.config["MYSQL_LOCAL_USER"],
                    "password": current_app.config["MYSQL_LOCAL_PASSWORD"],
                    "database": current_app.config["MYSQL_LOCAL_DB"],
                    "port": int(current_app.config["MYSQL_LOCAL_PORT"])
                }
            self.connection = pymysql.connect(
                host=self.conn_conf.get("host"),
                user=self.conn_conf.get("user"),
                password=self.conn_conf.get("password"),
                database=self.conn_conf.get("database"),
                charset='utf8mb4',
                port=self.conn_conf.get("port"),
                cursorclass=pymysql.cursors.DictCursor,
                client_flag=CLIENT.MULTI_STATEMENTS
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except Exception:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (self.connection is not None) and (self.cursor is not None):
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        if exc_type or exc_val or exc_tb:
            print("MySQL exc_type:", exc_type)
            print("MySQL exc_val:", exc_val)
            print("MySQL exc_tb:", exc_tb)
            return None
        return True


def read_query_from_file(file_path: str, params: dict):
    """
    The function reads the request from the file and inserts the params into it.

    :param file_path: str. A path to the file.
    :param params: dict. Query parameters.
    :return: str. Formatted SQL query.
    """
    with open(file_path, 'r') as sql_query:
        sql_query = sql_query.read()
        # Variable substitution in the sql_query
        return Template(sql_query).substitute(params)


def db_query(file_path: str, **params):
    """
    The function executes a database query and returns a response.

    :param file_path: str. A path to the file.
    :param params: dict. Query parameters.
    :return: list / None. Query results.
    """
    with DatabaseConnection() as cursor:
        sql_query = read_query_from_file(file_path=file_path, params=params)
        cursor.execute(sql_query)
        return cursor.fetchall()
