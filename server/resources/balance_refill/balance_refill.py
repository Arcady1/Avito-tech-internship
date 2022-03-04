# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse

# Project Modules
from server.resources.balance_status.balance_status import BalanceStatus
from server.db.work_with_db import db_query


class BalanceRefill(BalanceStatus, Resource):
    """ Class for working with the client's balance for refill. """

    def __init__(self):
        BalanceStatus.__init__(self)
        self.SQL_PATH_REFILL = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.amount = 0

    def put(self):
        """
        TODO
        :return:
        """
        # Server response
        response = self.get_user_balance()[0].copy()
        if response["status"] >= 400:
            return response, response["status"]

        parser = reqparse.RequestParser()
        parser.add_argument("amount", required=True)
        args = parser.parse_args()

        # 'Amount' data type check
        try:
            self.amount = float(args["amount"])
            if self.amount < 0:
                raise ValueError("Error: amount value must be more than zero")
            response["data"]["amount"] = self.amount
        except Exception as err:
            response["status"] = 400
            response["message"] = "Error: amount type must be float and the value must be more than zero"
            response["description"] = str(err)
            return response, response["status"]

        # Adding a user to the database and setting the balance
        if response["data"]["userBalance"] is None:
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "set_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                response["data"]["userBalance"] = self.amount
                response["message"] = "Success: the user is added to the DB and the balance is set"
            except Exception as err:
                response["status"] = 500
                response["message"] = "Error: adding the user to the DB and setting the balance"
                response["desciption"] = str(err)
                return response, response["status"]
        # Increasing user account balance
        else:
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "increase_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                response["data"]["userBalance"] = response["data"]["userBalance"] + self.amount
                response["message"] = "Success: user balance increase"
            except Exception as err:
                response["status"] = 500
                response["message"] = "Error: increasing user account balance"
                response["desciption"] = str(err)
                return response, response["status"]
        response["status"] = 201
        return response, response["status"]
