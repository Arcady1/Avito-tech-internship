# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource, reqparse

# Project Modules
from server.resources.balance_status.balance_status import BalanceStatus
from server.db.work_with_db import db_query
from server.utils import id_generator
from server.utils import modify_response


class BalanceRefill(BalanceStatus, Resource):
    """ Class for working with the client's balance for refill. """

    def __init__(self):
        BalanceStatus.__init__(self)
        self.SQL_PATH_REFILL = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.amount = 0
        self.transaction_id = id_generator()

    def check_amount_value(self, response):
        """
        The function checks the 'Amount' query argumnet.

        :param response: dict. Server response.
        :return: tuple. Response and response status.
        """
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

    def save_transaction_ids(self, response):
        """
        The function saves the user ID and transaction ID.

        :param response: dict. Server response.
        :return: tuple. Response and response status.
        """
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "save_transaction_ids.sql"),
                     user_id=self.user_id,
                     transaction_id=self.transaction_id)
            return response, 201
        except Exception as err:
            mes = "Error: adding the transaction to the db"
            modify_response(response=response, status=500, message=mes, error=err)
            return response, response["status"]

    def put(self):
        # Server response
        response = self.get_user_balance()[0].copy()
        if response["status"] >= 400:
            return response, response["status"]
        response = self.check_amount_value(response=response)[0]
        if response["status"] >= 400:
            return response, response["status"]

        # Adding a user to the database and setting the balance
        if response["data"]["userBalance"] is None:
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "set_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                response["data"]["userBalance"] = self.amount
                mes = "Success: the user is added to the DB and the balance is set"
                modify_response(response=response, status=201, message=mes)
            except Exception as err:
                mes = "Error: adding the user to the DB and setting the balance"
                modify_response(response=response, status=500, message=mes, error=err)
                return response, response["status"]
        # Increasing user account balance
        else:
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "increase_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                response["data"]["userBalance"] = response["data"]["userBalance"] + self.amount
                mes = "Success: user balance increase"
                modify_response(response=response, status=201, message=mes)
            except Exception as err:
                mes = "Error: increasing user account balance"
                modify_response(response=response, status=500, message=mes, error=err)
                return response, response["status"]

        # Saving the transaction to the DB
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "add_transaction.sql"),
                     user_id=self.user_id,
                     transaction_id=self.transaction_id,
                     type_="refill")
        except Exception as err:
            mes = "Error: saving the transaction to the db"
            modify_response(response=response, status=500, message=mes, error=err)
            return response, response["status"]

        # Saving the IDs of the transaction
        # Server response
        response = self.save_transaction_ids(response=response)[0]
        if response["status"] >= 400:
            return response, response["status"]
        return response, response["status"]
