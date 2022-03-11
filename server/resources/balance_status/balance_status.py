# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource
from pymysql.err import OperationalError, ProgrammingError

# Project Modules
from server.db.work_with_db import db_query
from server.utils import modify_response
from server.resources.balance.balance import Balance


class BalanceStatus(Balance, Resource):
    """ Class for working with the client's balance. """

    def __init__(self):
        Balance.__init__(self)
        self.SQL_PATH_STATUS = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.user_id = None

    def get_user_balance(self, query_argument_with_uid):
        """
        The function gets user's balance from the DB by ID.

        :return: tuple. Server response and status.
        """

        # Checking 'user_id' value
        self.user_id = self.check_user_id_value(query_argument=query_argument_with_uid)
        self.response["data"]["userId"] = self.user_id
        if self.response["status"] >= 400:
            return self.response, self.response["status"]

        # Getting a user's balance in the database by ID
        try:
            result = db_query(file_path=os.path.join(self.SQL_PATH_STATUS, "balance_status.sql"),
                              user_id=self.user_id)
            if result:
                self.response["data"]["userBalance"] = result[0]["balance"]
            mes = "Success: getting a user's balance in the database by ID"
            modify_response(response=self.response, status=200, message=mes)
        except AttributeError as err:
            mes = "Error: connecting to MySQL database"
            modify_response(response=self.response, status=400, message=mes, error=err)
        except OperationalError as err:
            mes = "Error: invalid MySQL database name"
            modify_response(response=self.response, status=400, message=mes, error=err)
        except ProgrammingError as err:
            mes = "Error: invalid MySQL syntax"
            modify_response(response=self.response, status=400, message=mes, error=err)
        except Exception as err:
            mes = "Error: working with MySQL database"
            modify_response(response=self.response, status=500, message=mes, error=err)
        return self.response, self.response["status"]

    def get(self):
        return self.get_user_balance(query_argument_with_uid="user_id")
