""" Project Launcher """

# Built-in Modules
import os

# Project Modules
from server.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=os.getenv("APP_PORT", 5000))
