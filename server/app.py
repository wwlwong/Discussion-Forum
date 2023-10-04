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

    def post(self):
        json=request.get_json()
        if session['user_id'] is None:
            return {"Error":"Unauthorized"}, 401
        
        new_reply= Post(
            title=json.get('title'),
            link=json.get('link'),
            expiry=json.get('expiry'),
            retailer=json.get('retailer'),
            category=json.get('category'),
            user_id = session['user_id'],
            upvotes = 0
         )

        retailer_tag = Tag.query.filter(Tag.name.lower() == json.get('retailer').lower()).first()
        if not retailer_tag:
            retailer_tag = Tag(name = json.get('retailer'))
            
        category_tag = Tag.query.filter(Tag.name.lower() == json.get('category').lower()).first()

        new_post.tagging.append(retailer_tag)
        new_post.tagging.append(category_tag)
        db.session.add(new_post)
        try:
            db.session.commit()
            return new_post.to_dict()
        except IntegrityError as e:
            db.session.rollback()
            return {"Error":"Unprocessable entity."}, 422   

class PostByID(Resource):
    def get(self, id):
        post = Post.query.filter(post.id=id).first()
        if not post:
            return {"error": "Post not found"}, 404
        post_dict = post.to_dict()
        response = make_response(post_dict, 200)
        return response

    def post(self, id):
        json=request.get_json()
        if session['user_id'] is None:
            return {"Error":"Unauthorized"}, 401

        new_reply = Reply(
            content = json.get('content'),
            post_id = id,
            user_id = session['user_id'],
            likes = 0
        )

        db.session.add(new_reply)
        db.session.commit()

        reply_dict = new_reply.to_dict()

        response = make_response(reply_dict, 200)
        return response

    
    def patch(self, id):
 
        user = User.query.filter(User.id == session['user_id']).first() 
        if user:
            if user.role_id == 1:
                post = Post.query.filter(Post.id=id, Post.user_id == session['user_id']).first()

            if user.role_id == 2 or user.role_id == 3:
                post = Post.query.filter(Post.id=id).first()
            
            if not post:
                return {"error": "Post not found"}, 404

            for attr in request.form:
                if attr == 'retailer':
                    old_retailer_tag = Tag.query.filter(Tag.name.lower() == post.retailer.lower())
                    new_retailer_tag = Tag.query.filter(Tag.name.lower() == request.form['retailer'])
                    if not new_retailer_tag:
                        new_retailer_tag = Tag(name = request.form['retailer'])
                    post.tagging.remove(old_retailer_tag)
                    post.tagging.append(new_retailer_tag)
                elif attr == 'category':
                    old_category_tag = Tag.query.filter(Tag.name == post.category)
                    new_category_tag = Tag.query.filter(Tag.name == request.form['category'])
                    post.tagging.remove(old_category_tag)
                    post.tagging.append(new_category_tag)
                else:
                    setattr(post, attr, request.form[attr])

            db.session.add(post)
            db.session.commit()

            post_dict = post.to_dict()

            response = make_response(post_dict, 200)
            return response    

        return {"Error":"Unauthorized"}, 401

    def delete(self, id):
        if session['user_id']:
            user = User.query.filter(User.id == session['user_id']).first()
            if user.role_id == 2 or user.role_id == 3:
                post = Post.query.filter(Post.id=id).first()
            else:
                post = Post.query.filter(Post.id=id, Post.user_id = user.id).first()

            if not post:
                return {"error": "Post not found"}, 404

            db.session.delete(post)
            db.session.commit()

            response = make_response("", 204)

            return response    
        return {"Error":"Unauthorized"}, 401 

class UserByID(Resource):

    def patch (self,id):
        if session['user_id'] != id:
            return {"Error":"Unauthorized"}, 401
        
        user = User.query.filter(User.id == id).first()
        if not user:
            return {"error": "User not found"}, 404

        for attr in request.form:
            setattr(user, attr, request.form[attr])
        
        db.session.add(user)
        db.session.commit()

        user_dict = user.to_dict()

        response = make_response(user_dict, 200)
        return response    

    def delete(self, id):
        admin = User.query.filter(User.id == session['user_id']).first()
        if admin.role_id != 3:
            return {"Error":"Unauthorized"}, 401
        user = User.query.filter(User.id == id).first()
        if not user:
            return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()

        response = make_response("", 204)

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
api.add_resource(PostByID, '/post/<int:id>')
api.add_resource(UserByID, '/user/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)