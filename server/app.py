from flask import request, session, make_response
from flask_restful import Resource

from config import app, db, api # This line will run the config.py file and initialize our app
from models import User, Post, Role, Reply


# All routes here!







if __name__ == '__main__':
    app.run(port=4000, debug=True)