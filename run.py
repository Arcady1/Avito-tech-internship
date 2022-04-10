""" Project Launcher """

# Third Party Modules
from dotenv import load_dotenv

# Project Modules
from server.app import create_app

load_dotenv()

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
