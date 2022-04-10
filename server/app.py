# Built-in Modules
import os

# Third Party Modules
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

# Project Modules
from server.resources.balance_refill.balance_refill import BalanceRefill
from server.resources.balance_status.balance_status import BalanceStatus
from server.resources.balance_writeoff.balance_writeoff import BalanceWriteoff
from server.resources.money_transfer.money_transfer import MoneyTransfer
from server.resources.detailed_transactions.detailed_transactions import DetailedTransactions

load_dotenv(find_dotenv())


def create_app(test_mode: bool = False):
    """
    The function creates a Flask App

    :param test_mode: bool. The flag indicates the mode of the application.
    :return: flask.app.Flask. Flask application.
    """
    app = Flask(__name__)

    main_config = {
        "SECRET_KEY": os.getenv("SECRET_KEY_DEV"),
        "MYSQL_LOCAL_HOST": os.getenv("MYSQL_LOCAL_HOST_DEV"),
        "MYSQL_LOCAL_USER": os.getenv("MYSQL_LOCAL_USER_DEV"),
        "MYSQL_LOCAL_PASSWORD": os.getenv("MYSQL_LOCAL_PASSWORD_DEV"),
        "MYSQL_LOCAL_DB": os.getenv("MYSQL_LOCAL_DB_DEV"),
        "MYSQL_LOCAL_PORT": os.getenv("MYSQL_LOCAL_PORT_DEV")
    }
    testing_config = {
        "SECRET_KEY": os.getenv("SECRET_KEY_TEST"),
        "ENV": "development",
        "TESTING": True,
        "MYSQL_LOCAL_DB": os.getenv("MYSQL_LOCAL_DB_TEST")
    }

    app.config.update(main_config)

    if test_mode:
        app.config.update(testing_config)

    api = Api(app)

    api.add_resource(BalanceStatus, '/api/v1.0/balance/users')
    api.add_resource(BalanceRefill, '/api/v1.0/refill/users')
    api.add_resource(BalanceWriteoff, '/api/v1.0/writeoff/users')
    api.add_resource(MoneyTransfer, '/api/v1.0/transfer/users')
    api.add_resource(DetailedTransactions, '/api/v1.0/transactions/users')

    return app
