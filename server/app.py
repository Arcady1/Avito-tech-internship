# Third Party Modules
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

# Project Modules
from server.resources.balance_refill.balance_refill import BalanceRefill
from server.resources.balance_status.balance_status import BalanceStatus
from server.resources.balance_writeoff.balance_writeoff import BalanceWriteoff
from server.resources.money_transfer.money_transfer import MoneyTransfer

load_dotenv()
app = Flask(__name__)
api = Api(app)

api.add_resource(BalanceStatus, '/api/v1.0/balance/users')
api.add_resource(BalanceRefill, '/api/v1.0/refill/users')
api.add_resource(BalanceWriteoff, '/api/v1.0/writeoff/users')
api.add_resource(MoneyTransfer, '/api/v1.0/transfer/users')
