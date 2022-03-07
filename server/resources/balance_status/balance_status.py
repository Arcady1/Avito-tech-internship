# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse
from pymysql.err import OperationalError, ProgrammingError

# Project Modules
from server.db.work_with_db import db_query
from server.utils import modify_response


class BalanceStatus(Resource):
    """ Class for working with the client's balance. """

    def __init__(self):
        self.SQL_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.user_id = None

    def get_user_balance(self):
        """
        The function gets user's balance from the DB by ID.

        :return: tuple. Server response and status.
        """
        # Server response
        response = {
            "status": None,
            "message": "",
            "description": "",
            "data": {
                "userId": None,
                "userBalance": None,
            }
        }
        parser = reqparse.RequestParser()
        parser.add_argument("user_id", required=True)
        args = parser.parse_args()

        # 'UserId' data type check
        try:
            self.user_id = int(args["user_id"])
            if self.user_id < 0:
                raise ValueError("Error: user_id value must be more than zero")
            response["data"]["userId"] = self.user_id
        except Exception as err:
            mes = "Error: user_id type must be integer and the value must be more than zero"
            modify_response(response=response, status=400, message=mes, error=err)
            return response, response["status"]

        # Getting a user's balance in the database by ID
        try:
            result = db_query(file_path=os.path.join(self.SQL_PATH, "balance_status.sql"),
                              user_id=self.user_id)
            if result:
                response["data"]["userBalance"] = result[0]["balance"]
            mes = "Success: getting a user's balance in the database by ID"
            modify_response(response=response, status=200, message=mes)
        except AttributeError as err:
            mes = "Error: connecting to MySQL database"
            modify_response(response=response, status=400, message=mes, error=err)
        except OperationalError as err:
            mes = "Error: invalid MySQL database name"
            modify_response(response=response, status=400, message=mes, error=err)
        except ProgrammingError as err:
            mes = "Error: invalid MySQL syntax"
            modify_response(response=response, status=400, message=mes, error=err)
        except Exception as err:
            mes = "Error: working with MySQL database"
            modify_response(response=response, status=500, message=mes, error=err)
        return response, response["status"]

    def get(self):
        return self.get_user_balance()
