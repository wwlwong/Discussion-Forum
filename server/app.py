from flask import request, session, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api # This line will run the config.py file and initialize our app
from models import User, Post, Role, Reply, Tag


# All routes here!

class Homepage(Resource):
    def get(self):
        return 'Welcome to Hot Deals: A discussion forum for all deals'




api.add_resource(Homepage, '/', endpoint='/')

if __name__ == '__main__':
    app.run(port=4000, debug=True)