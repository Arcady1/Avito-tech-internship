# Built-in Modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource

# Project Modules
from server.resources.balance.balance import Balance
from server.db.work_with_db import db_query
from server.utils import id_generator
from server.utils import modify_response


class MoneyTransfer(Balance, Resource):
    """ Class for working with money transfer. """

    def __init__(self):
        Balance.__init__(self)
        self.SQL_PATH_MONEY_TRANSFER = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.response["data"]["sender"] = {
            "id": None,
            "balance": None
        }
        self.response["data"]["receiver"] = {
            "id": None,
            "balance": None
        }
        del self.response["data"]["userId"]
        del self.response["data"]["userBalance"]
        self.response["data"]["amount"] = None
        self.transaction_id = id_generator()
        self.sender_uid = None
        self.sender_balance = None
        self.receiver_uid = None
        self.receiver_balance = None
        self.amount = 0

    def put(self):
        # Getting user balance by 'sender_uid'
        self.sender_uid, self.sender_balance = self.get_user_balance(query_argument_with_uid="sender_uid")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["sender"]["id"] = self.sender_uid
        self.response["data"]["sender"]["balance"] = self.sender_balance

        # Getting user balance by 'receiver_uid'
        self.receiver_uid, self.receiver_balance = self.get_user_balance(query_argument_with_uid="receiver_uid")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["receiver"]["id"] = self.receiver_uid
        self.response["data"]["receiver"]["balance"] = self.receiver_balance

        # If user ID is not found
        if (self.sender_balance is None) or (self.receiver_balance is None):
            non_uid = self.sender_uid
            if self.sender_balance is not None: non_uid = self.receiver_uid
            mes = f"Error: the user ID={non_uid} is not found"
            modify_response(response=self.response, status=400, message=mes)
            return self.response, self.response["status"]

        # Cheking the 'amount' value
        self.amount = self.check_amount_value(query_argument_with_amount="amount")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["amount"] = self.amount

        # Checking if the amount more than sender balance
        if self.sender_balance < self.amount:
            mes = f"Error: the user balance must be more than amount value"
            modify_response(response=self.response, status=400, message=mes)
            return self.response, self.response["status"]

        # Money transfer
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_MONEY_TRANSFER, "money_transfer.sql"),
                     sender_uid=self.sender_uid,
                     receiver_uid=self.receiver_uid,
                     sender_balance=self.sender_balance,
                     receiver_balance=self.receiver_balance,
                     amount=self.amount)
            self.response["data"]["sender"]["balance"] = self.sender_balance - self.amount
            self.response["data"]["receiver"]["balance"] = self.receiver_balance + self.amount
            mes = "Success: money transfer"
            modify_response(response=self.response, status=200, message=mes)
        except Exception as err:
            mes = "Error: money transfer"
            modify_response(response=self.response, status=500, message=mes, error=err)
            return self.response, self.response["status"]

        # Saving the transaction to the DB
        try:
            db_query(file_path=os.path.join(self.SQL_PATH_MONEY_TRANSFER, "add_transaction.sql"),
                     transaction_id=self.transaction_id,
                     sender_uid=self.sender_uid,
                     receiver_uid=self.receiver_uid,
                     type_="Money transfer",
                     amount=self.amount)
        except Exception as err:
            mes = "Error: saving the transaction to the db, BUT money transfer is completed"
            modify_response(response=self.response, status=500, message=mes, error=err)
            return self.response, self.response["status"]

        # Saving the IDs of the transaction
        for uid in (self.sender_uid, self.receiver_uid):
            self.save_transaction_ids(user_id=uid,
                                      transaction_id=self.transaction_id)
            if self.response["status"] >= 400:
                return self.response, self.response["status"]

        return self.response, self.response["status"]
