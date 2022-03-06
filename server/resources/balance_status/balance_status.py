# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse
from pymysql.err import OperationalError, ProgrammingError

# Project Modules
from server.db.work_with_db import db_query


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
            response["status"] = 400
            response["message"] = "Error: user_id type must be integer and the value must be more than zero"
            response["description"] = str(err)
            return response, response["status"]

        # Getting a user's balance in the database by ID
        try:
            result = db_query(file_path=os.path.join(self.SQL_PATH, "balance_status.sql"),
                              user_id=self.user_id)
            if result:
                response["data"]["userBalance"] = result[0]["balance"]
            response["status"] = 200
            response["message"] = "Success: getting a user's balance in the database by ID"
        except AttributeError as err:
            response["status"] = 400
            response["message"] = "Error: connecting to MySQL database"
            response["description"] = str(err)
        except OperationalError as err:
            response["status"] = 400
            response["message"] = "Error: invalid MySQL database name"
            response["description"] = str(err)
        except ProgrammingError as err:
            response["status"] = 400
            response["message"] = "Error: invalid MySQL syntax"
            response["description"] = str(err)
        except Exception as err:
            response["message"] = "Error: working with MySQL database"
            response["description"] = str(err)
            response["status"] = 500
        return response, response["status"]

    def get(self):
        return self.get_user_balance()
