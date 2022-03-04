# Third Party Modules
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

# Project Modules
from server.resources.balance_refill.balance_refill import BalanceRefill
from server.resources.balance_status.balance_status import BalanceStatus

load_dotenv()
app = Flask(__name__)
api = Api(app)

api.add_resource(BalanceStatus, '/api/v1.0/balance/users')
api.add_resource(BalanceRefill, '/api/v1.0/refill/users')
