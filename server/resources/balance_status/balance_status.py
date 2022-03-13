# Third Party Modules
from flask_restful import Resource

# Project Modules
from server.resources.balance.balance import Balance


class BalanceStatus(Balance, Resource):
    """ Class for working with the client's balance. """

    def __init__(self):
        Balance.__init__(self)
        self.user_id = None
        self.user_balance = None

    def get(self):
        self.user_id, self.user_balance = self.get_user_balance(query_argument_with_uid="user_id")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["userId"] = self.user_id
        self.response["data"]["userBalance"] = self.user_balance

        return self.response, self.response["status"]
