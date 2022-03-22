# Built-in Modules
import os

# Third Party Modules
from flask_restful import Resource, reqparse
import requests

# Project Modules
from server.resources.balance.balance import Balance
from server.utils import modify_response


class BalanceStatus(Balance, Resource):
    """ Class for working with the client's balance. """

    def __init__(self):
        Balance.__init__(self)
        self.user_id = None
        self.user_balance = None
        self.currency = "RUB"

    def transform_currency(self, query_argument_with_currency: str, amount_RUB: float):
        """
        The function converts RUB to 'currency'.
        The function modifies a response.

        :param query_argument_with_currency: str. The name of query parametr with a 'currency'.
        :param amount_RUB: float. Amount of money to convert.
        :return: tuple. Converted amount and currency.
        """
        parser = reqparse.RequestParser()
        parser.add_argument(query_argument_with_currency, required=False)
        args = parser.parse_args()
        to_currency = args[query_argument_with_currency]

        if to_currency is None:
            return (amount_RUB, "RUB")
        to_currency = to_currency.upper()
        if to_currency == "RUB":
            return (amount_RUB, "RUB")

        # Transfer balance to 'currency'
        try:
            url = "https://api.getgeoapi.com/v2/currency/convert"
            querystring = {"api_key": os.getenv("CURRENCY_CONVERTER_API_KEY"),
                           "from": "RUB",
                           "to": to_currency,
                           "amount": amount_RUB,
                           "format": "json"}
            resp = requests.get(url=url,
                                params=querystring)
            resp = resp.json()
            if resp["status"] == "failed":
                raise ValueError(resp["error"]["message"])
            if not resp["rates"]:
                raise ValueError("Error: check the query parameters")

            transfered_balance = resp["rates"][to_currency]["rate_for_amount"]
            self.response["status"] = 200
            return (float(transfered_balance), to_currency)
        except Exception as err:
            mes = f"Error: transfering user balance to '{to_currency}'"
            modify_response(response=self.response, status=400, message=mes, error=err)
            return (amount_RUB, "RUB")

    def get(self):
        # Getting user balance by 'user_id'
        self.user_id, self.user_balance = self.get_user_balance(query_argument_with_uid="user_id")
        if self.response["status"] >= 400:
            return self.response, self.response["status"]
        self.response["data"]["userId"] = self.user_id

        # None to 0
        self.user_balance = self.user_balance or float(0)

        transfered_balance, currency = self.transform_currency(query_argument_with_currency="currency",
                                                               amount_RUB=self.user_balance)
        self.response["data"]["userBalance"] = transfered_balance
        self.response["data"]["currency"] = currency

        return self.response, self.response["status"]
