from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String)
    email = db.Column(db.String)
    verified = db.Column(db.String, default=False)
    joined_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    posts = db.relationship('Post', backref='user')
    replies = db.relationship('Reply', backref='user')
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    serialize_rules = (
        'posts.user',
        'replies.user',
    )

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("failed simple email validation")
        return address

    def __repr__(self):
        return f"\n<User id={self.id} username={self.username} email={self.email} role={self.role_id}>"


class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String, nullable=False)
    users = db.relationship('User', backref='role')

    serialize_rules = (
        'users.role',
    )
    
    def __repr__(self):
        return f"\n<Role id={self.id} Role={self.role_name}>"



class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String)
    expiry = db.Column(db.String)
    retailer = db.Column(db.String)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    upvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    serialize_rules = (
        'user.posts',
    )

    def __repr__(self):
        return f"\n<Post id={self.id} title={self.title}, user={self.user_id} >"


class Reply(db.Model, SerializerMixin):
    __tablename__ = 'replies'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    likes = db.Column(db.Integer, default=0)

    serialize_rules = (
        'user.replies',
    )

    def __repr__(self):
        return f"\n<Reply id={self.id} post={self.post_id}, user={self.user_id} >"
