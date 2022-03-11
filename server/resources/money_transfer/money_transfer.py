# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse

# Project Modules
from server.resources.balance_refill.balance_refill import BalanceRefill
from server.db.work_with_db import db_query
from server.utils import id_generator
from server.utils import modify_response


class MoneyTransfer(Resource):
    """ Class for working with money transfer. """

    def __init__(self):
        pass

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("amount", required=True)
        args = parser.parse_args()

        # 'Amount' data type check
        try:
            self.amount = float(args["amount"])
            if self.amount < 0:
                raise ValueError("Error: amount value must be more than zero")
            response["data"]["amount"] = self.amount
            return response, 200
        except Exception as err:
            mes = "Error: amount type must be float and the value must be more than zero"
            modify_response(response=response, status=400, message=mes, error=err)
            return response, response["status"]