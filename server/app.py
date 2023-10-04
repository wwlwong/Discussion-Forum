from flask import request, session, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from config import app, db, api # This line will run the config.py file and initialize our app
from models import User, Post, Role, Reply, Tag


# All routes here!

class Homepage(Resource):
    def get(self):
        return 'Welcome to Hot Deals: A discussion forum for all deals'

class Signup(Resource):
    def post(self):
        data = request.get_json()

        user = User( 
            username=data["username"],
            email=data["email"],
            role_id = 1
        )
        user.password_hash = data['password']
        try: 
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict(), 201
        except IntegrityError as e:

            errors = [] # List for collecting all errors

						# Required key to be sent from client
            required_keys = ['username', 'email', 'password', 'password_confirmation'] 

						# If value is empty string, append message to errors
            for key in required_keys:
                if not data[key]:
                    errors.append(f"{key} is required")

						# If password confirmation does not match provided password, append error message to errors list
            if data['password'] != data['password_confirmation']:
                errors.append('Password  confirmation failed')
         
                
            # Check if the error is an IntegrityError or DataError
            if isinstance(e, (IntegrityError)):
                for error in e.orig.args:
                    errors.append(str(error))# Get the error message as a string

            return {'errors': errors}, 422

class Login(Resource):

    def post(self):

        username = request.get_json()['username']
        password = request.get_json()['password']

        user = User.query.filter(User.username == username).first()

        if user.authenticate(password):

            session['user_id'] = user.id
            return user.to_dict(), 200

        return {'error': '401 Unauthorized'}, 401

class CheckSession(Resource):

    def get(self):

        if session.get('user_id'):
            
            user = User.query.filter(User.id == session['user_id']).first()
            
            return user.to_dict(), 200

        return {}, 204


class Logout(Resource):
    def delete(self):
         if session['user_id']:
            session['user_id']=None
            return {"message":"Successfully logged out."}, 204
        else:
            return {"message":"User not logged in."}, 401


class Tag(Resource):
    def post(self):
        if session['user_id']:
            form_json = request.get_json()
            
            new_tag = Tag(
                name=form_json["name"]
            )
            db.session.add(new_tag)
            db.session.commit()

            response_dict = new_tag.to_dict()

            response = make_response(
                response_dict,
                201,
            )
            return response
        return {"Error":"Unauthorized"}, 401

class TagByID(Resource):

    def delete(self, id):
        user = User.query.filter(User.id == session['user_id']).first() 
        if user.role_id == 2 or user.role_id == 3:
            tag = Tag.query.filter_by(id=id).first()
            if not tag:
                return {"error": "Tag not found"}, 404
            db.session.delete(tag)
            db.session.commit()

            response = make_response("", 204)

            return response 
        return {"Error":"Unauthorized"}, 401    


class ReplyByID(Resource):

    def patch(self, id):
        user = User.query.filter(User.id == session['user_id']).first() 
        if user:
            if user.role_id == 1:
                reply = Reply.query.filter(Reply.id=id, Reply.user_id == session['user_id']).first()
                if not reply:
                return {"error": "Reply not found"}, 404
            if user.role_id == 2 or user.role_id == 3:
                reply = Reply.query.filter(Reply.id=id).first()
                if not reply:
                    return {"error": "Reply not found"}, 404

            for attr in request.form:
                setattr(reply, attr, request.form[attr])

            db.session.add(reply)
            db.session.commit()

            reply_dict = reply.to_dict()

            response = make_response(reply_dict, 200)
            return response
        
        return {"Error":"Unauthorized"}, 401 


    def delete(self,id):
        
        user = User.query.filter(User.id == session['user_id']).first() 
        if user:
            if user.role_id == 1:
                reply = Reply.query.filter(Reply.id=id, Reply.user_id == session['user_id']).first()

            if user.role_id == 2 or user.role_id == 3:
                reply = Reply.query.filter(Reply.id=id).first()
            
            if not reply:
                return {"error": "Reply not found"}, 404

            db.session.delete(reply)
            db.session.commit()

            response = make_response("", 204)

            return response    
        return {"Error":"Unauthorized"}, 401 

class Post(Resource):
    
    def get(self):
        post_list = [p.to_dict() for p in Post.query.all()]
        response = make_response(
            post_list,
            200,
        )

        return response

    


api.add_resource(Homepage, '/', endpoint='/')
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Tag, '/tag', endpoint='tag')
api.add_resource(TagByID, "/tag/<int:id>")
api.add_resource(ReplyByID, '/reply/<int:id>')
api.add_resource(Post, '/post', endpoint='post')

if __name__ == '__main__':
    app.run(port=5555, debug=True)