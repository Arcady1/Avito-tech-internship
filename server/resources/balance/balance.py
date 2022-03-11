# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse

# Project Modules
from server.db.work_with_db import db_query
from server.utils import modify_response


class Balance(Resource):
    def __init__(self):
        # Server response
        self.response = {
            "status": None,
            "message": None,
            "description": None,
            "data": {
                "userId": None,
                "userBalance": None,
            }
        }
        self.MAIN_SQL_PATH = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")

    def check_amount_value(self):
        """ The function checks the 'amount' query argumnet. """
        parser = reqparse.RequestParser()
        parser.add_argument("amount", required=True)
        args = parser.parse_args()

        # 'Amount' data type check
        try:
            self.amount = float(args["amount"])
            if self.amount < 0:
                raise ValueError("Error: amount value must be more than zero")
            self.response["data"]["amount"] = self.amount
            self.response["status"] = 200
        except Exception as err:
            mes = "Error: amount type must be float and the value must be more than zero"
            modify_response(response=self.response, status=400, message=mes, error=err)

    def check_user_id_value(self, query_argument):
        """
        The function checks the 'user_id' query argumnet.

        :param query_argument: str. The name of the argument with user id.
        :return: int. The user id.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(query_argument, required=True)
        args = parser.parse_args()

        # 'UserId' data type check
        try:
            id = int(args[query_argument])
            if id < 0:
                raise ValueError("Error: user_id value must be more than zero")
            self.response["status"] = 200
            return id
        except Exception as err:
            mes = "Error: user_id type must be integer and the value must be more than zero"
            modify_response(response=self.response, status=400, message=mes, error=err)

    def save_transaction_ids(self):
        """ The function saves the user ID and transaction ID. """
        try:
            db_query(file_path=os.path.join(self.MAIN_SQL_PATH, "save_transaction_ids.sql"),
                     user_id=self.user_id,
                     transaction_id=self.transaction_id)
            self.response["status"] = 200
        except Exception as err:
            mes = "Error: adding the transaction to the db"
            modify_response(response=self.response, status=500, message=mes, error=err)
