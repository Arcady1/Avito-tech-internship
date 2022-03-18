# Built-in Modules
import pathlib, os

# Third Party Modules
from flask_restful import Resource

# Project Modules
from server.resources.balance.balance import Balance
from server.db.work_with_db import db_query
from server.utils import modify_response


class DetailedTransactions(Balance, Resource):
    def __init__(self):
        Balance.__init__(self)
        self.SQL_PATH_DETAILED_TRANSACTIONS = os.path.join(pathlib.Path(__file__).parent.resolve(), "sql")
        self.user_id = None
        self.response["data"] = {
            "userId": None,
            "transactions": []
        }

    def prepare_data(self, data: list):
        """
        The function prepares data for response.

        :param data: list. Input data. All users' transaction.
        :return: list. Output data. Prepared users' transaction.
        """
        prepared_data = []
        for el in data:
            tmpl = {
                "transactionName": el["type_"],
                "amount": el["amount"],
                "date": el["date_"].strftime("%Y-%m-%d, %H:%M:%S")
            }
            if el["type_"] == "Money transfer":
                tmpl["senderUid"] = el["sender_uid"]
                tmpl["recieverUid"] = el["reciever_uid"]
            prepared_data.append(tmpl)
        return prepared_data

    def get(self):
        # Getting all users' transactions by 'user_id'
        self.user_id = self.check_user_id_value(query_argument="user_id")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["userId"] = self.user_id

        # Getting the list of transactions
        try:
            data = db_query(file_path=os.path.join(self.SQL_PATH_DETAILED_TRANSACTIONS, "detailed_transactions.sql"),
                            user_id=self.user_id)
            prepared_data = self.prepare_data(data=data)
            self.response["data"]["transactions"] = prepared_data

            mes = "Success: getting users' detailed transactions"
            modify_response(response=self.response, status=200, message=mes)
            return self.response, self.response["status"]
        except Exception as err:
            mes = "Error: getting users' detailed transactions"
            modify_response(response=self.response, status=500, message=mes, error=err)
            return self.response, self.response["status"]
