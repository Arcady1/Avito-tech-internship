# Built-in Modules
import pathlib, os

# Third Party Modules
import flask_restful
from flask_restful import Resource, reqparse
from pymysql.err import OperationalError, ProgrammingError

# Project Modules
from server.db.work_with_db import db_query
from server.utils import modify_response


class Balance(Resource):
    def __init__(self):
        # Server response
        self.response = {
            "status": None,
            "message": None,
            "description": "",
            "data": {
                "userId": None,
                "userBalance": None,
                "currency": "RUB"
            }
        }
        self.SQL_PATH_MAIN = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")

    def check_amount_value(self, query_argument_with_amount: str):
        """
        The function checks the 'amount' query argumnet.
        The function modifies a response.

        :param query_argument_with_amount: str. The name of query parametr with an amount.
        :return: float / None. Value of 'amount' argumnet.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(query_argument_with_amount)
        args = parser.parse_args()
        message_error = "Error: amount is a required parameter"
        description_error = "Enter an amount"

        # Check if query_argument is empty
        if args[query_argument_with_amount] is None:
            flask_restful.abort(http_status_code=400,
                                status=400,
                                message=message_error,
                                description=description_error)

        # 'Amount' data type check
        try:
            amount = float(args[query_argument_with_amount])
            if amount < 0.000001:
                raise ValueError("Error: amount value must be more than zero")
            self.response["status"] = 200
            return amount
        except Exception as err:
            mes = "Error: amount type must be float and the value must be more than zero"
            modify_response(response=self.response, status=400, message=mes, error=err)
            return

    def check_user_id_value(self, query_argument: str):
        """
        The function checks the 'user_id' query argumnet.
        The function modifies a response.

        :param query_argument: str. The name of query parametr with a user ID.
        :return: int / None. The user id.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(query_argument)
        args = parser.parse_args()
        message_error = "Error: user_id is a required parameter"
        description_error = "Enter a user ID"

        # Check if query_argument is empty
        if args[query_argument] is None:
            flask_restful.abort(http_status_code=400,
                                status=400,
                                message=message_error,
                                description=description_error)

        # 'UserId' data type check
        try:
            id = int(args[query_argument])
            if id < 1:
                raise ValueError("Error: user_id value must be more than zero")
            self.response["status"] = 200
            return id
        except Exception as err:
            mes = "Error: user_id type must be integer and the value must be more than zero"
            modify_response(response=self.response, status=400, message=mes, error=err)
            return

    def save_transaction_ids(self, user_id: int, transaction_id: int):
        """
        The function saves the user ID and transaction ID.
        The function modifies a response.

        :param user_id: int. The user ID
        :param transaction_id: The transaction ID
        """
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_MAIN, "save_transaction_ids.sql"),
                     user_id=user_id,
                     transaction_id=transaction_id)
            if not self.response["status"]:
                self.response["status"] = 200
        except Exception as err:
            mes = "Error: adding the transaction to the db"
            modify_response(response=self.response, status=500, message=mes, error=err)

    def get_user_balance(self, query_argument_with_uid: str):
        """
        The function gets users' balance from the DB by ID.
        The function modifies a response.

        :param query_argument_with_uid: str. The name of query parametr with a user ID.
        :return: tuple. User ID and the balance.
        """

        # Checking 'query_argument_with_uid' value
        user_id = self.check_user_id_value(query_argument=query_argument_with_uid)
        if user_id is None:
            return (user_id, None)

        # Getting a user's balance in the database by ID
        try:
            result = db_query(file_path=os.path.join(self.SQL_PATH_MAIN, "balance_status.sql"),
                              user_id=user_id)
            if len(result) > 1:
                raise ValueError(f"Error: there are {len(result)} users with id={user_id} in a DB")
            elif len(result) == 1:
                mes = "Success: getting a users' balance in the database by ID"
                modify_response(response=self.response, status=200, message=mes)
                return (user_id, result[0]["balance"])
            elif not result:
                mes = f"Warning: user with id={user_id} not found"
                modify_response(response=self.response, status=200, message=mes)
                return (user_id, None)
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

        return (user_id, None)
