from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    pass

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    
    pass

class Reply(db.Model, SerializerMixin):
    __tablename__ = 'replies'
    
    pass