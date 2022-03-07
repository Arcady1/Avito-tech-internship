# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource

# Project Modules
from server.resources.balance_refill.balance_refill import BalanceRefill
from server.db.work_with_db import db_query
from server.utils import id_generator
from server.utils import modify_response


class BalanceWriteoff(BalanceRefill, Resource):
    """ Class for working with the client's balance for write-off. """

    def __init__(self):
        BalanceRefill.__init__(self)
        self.SQL_PATH_WRITEOFF = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.balance_after_debit = None
        self.transaction_id = id_generator()

    def put(self):
        # Server response
        response = self.get_user_balance()[0].copy()
        if response["status"] >= 400:
            return response, response["status"]
        response = self.check_amount_value(response=response)[0]
        if response["status"] >= 400:
            return response, response["status"]

        # If the amount greater than the user's balance
        try:
            if self.amount > response["data"]["userBalance"]:
                raise ValueError("Error: the debit amount cannot exceed the user's balance")
            self.balance_after_debit = response["data"]["userBalance"] - self.amount
            response["data"]["userBalance"] = self.balance_after_debit
        except Exception as err:
            mes = "Error: wrong debit amount"
            modify_response(response=response, status=400, message=mes, error=err)
            return response, response["status"]

        # Change the user balance
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_WRITEOFF, "balance_writeoff.sql"),
                     balance_after_debit=self.balance_after_debit,
                     uid=self.user_id)
            mes = "Success: the debit was successful"
            modify_response(response=response, status=201, message=mes)
        except Exception as err:
            mes = "Error: changing the user balance"
            modify_response(response=response, status=400, message=mes, error=err)
            return response, response["status"]

        # Saving the transaction to the DB
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_WRITEOFF, "add_transaction.sql"),
                     user_id=self.user_id,
                     transaction_id=self.transaction_id,
                     type_="write-off")
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
