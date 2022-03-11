# Built-in modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource

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
        self.transaction_id = id_generator()
        self.user_id = None
        self.amount = 0

    def put(self):
        # Getting user balance by 'user_id'
        self.get_user_balance(query_argument_with_uid="user_id")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]

        # Cheking the 'amount' value
        self.check_amount_value()
        if self.response["status"] >= 400:
            return self.response, self.response["status"]

        # Adding a user to the database and setting the balance
        if self.response["data"]["userBalance"] is None:
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "set_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                self.response["data"]["userBalance"] = self.amount
                mes = "Success: the user is added to the DB and the balance is set"
                modify_response(response=self.response, status=201, message=mes)
            except Exception as err:
                mes = "Error: adding the user to the DB and setting the balance"
                modify_response(response=self.response, status=500, message=mes, error=err)
                return self.response, self.response["status"]
        # Increasing user account balance
        else:
            print("self.user_id", self.user_id)
            print("self.amount", self.amount)
            try:
                db_query(file_path=os.path.join(self.SQL_PATH_REFILL, "increase_balance.sql"),
                         user_id=self.user_id,
                         amount=self.amount)
                self.response["data"]["userBalance"] = self.response["data"]["userBalance"] + self.amount
                mes = "Success: user balance increase"
                modify_response(response=self.response, status=201, message=mes)
            except Exception as err:
                mes = "Error: increasing user account balance"
                modify_response(response=self.response, status=500, message=mes, error=err)
                return self.response, self.response["status"]

        # Saving the transaction to the DB
        try:
            db_query(file_path=os.path.join(self.MAIN_SQL_PATH, "add_transaction.sql"),
                     user_column="reciever_uid",
                     user_id=self.user_id,
                     transaction_id=self.transaction_id,
                     type_="refill")
        except Exception as err:
            mes = "Error: saving the transaction to the db"
            modify_response(response=self.response, status=500, message=mes, error=err)
            return self.response, self.response["status"]

        # Saving the IDs of the transaction
        self.save_transaction_ids()
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        return self.response, self.response["status"]
