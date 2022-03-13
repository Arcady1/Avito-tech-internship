# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource

# Project Modules
from server.resources.balance.balance import Balance
from server.db.work_with_db import db_query
from server.utils import id_generator
from server.utils import modify_response


class BalanceWriteoff(Balance, Resource):
    """ Class for working with the client's balance for write-off. """

    def __init__(self):
        Balance.__init__(self)
        self.SQL_PATH_WRITEOFF = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.user_balance = None
        self.transaction_id = id_generator()
        self.user_id = None
        self.amount = 0

    def put(self):
        # Getting user balance by 'user_id'
        self.user_id, self.user_balance = self.get_user_balance(query_argument_with_uid="user_id")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["userId"] = self.user_id
        self.response["data"]["userBalance"] = self.user_balance

        # Cheking the 'amount' value
        self.amount = self.check_amount_value(query_argument_with_amount="amount")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["amount"] = self.amount

        # If the amount greater than the user's balance
        try:
            if self.amount > self.response["data"]["userBalance"]:
                raise ValueError("Error: the debit amount cannot exceed the user's balance")
        except Exception as err:
            mes = "Error: wrong debit amount"
            modify_response(response=self.response, status=400, message=mes, error=err)
            return self.response, self.response["status"]

        # Change the user balance
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_WRITEOFF, "balance_writeoff.sql"),
                     current_balance=self.user_balance,
                     amount=self.amount,
                     user_id=self.user_id)
            self.response["data"]["userBalance"] = self.response["data"]["userBalance"] - self.amount
            mes = "Success: write-off was successful"
            modify_response(response=self.response, status=201, message=mes)
        except Exception as err:
            mes = "Error: changing the user balance"
            modify_response(response=self.response, status=400, message=mes, error=err)
            return self.response, self.response["status"]

        # Saving the transaction to the DB
        try:
            db_query(file_path=os.path.join(self.MAIN_SQL_PATH, "add_transaction.sql"),
                     user_column="sender_uid",
                     user_id=self.user_id,
                     transaction_id=self.transaction_id,
                     type_="Write-off",
                     amount=self.amount)
        except Exception as err:
            mes = "Error: saving the transaction to the db, BUT userBalance is reduced."
            modify_response(response=self.response, status=500, message=mes, error=err)
            return self.response, self.response["status"]

        # Saving the IDs of the transaction
        self.save_transaction_ids(user_id=self.user_id,
                                  transaction_id=self.transaction_id)
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        return self.response, self.response["status"]
