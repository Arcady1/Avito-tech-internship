""" Project Launcher """

# Project modules
from server.app import app

if __name__ == "__main__":
    app.run(host='localhost', port=8080)
