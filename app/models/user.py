from datetime import datetime
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserRole:
    """Class containing constants for different user roles in the secure online voting system."""
    ADMIN = 'admin'
    VOTER = 'voter'

class User(db.Model):
    """Class representing a user in the secure online voting system.

    Attributes:
        id (int): The unique identifier of the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The hashed password of the user.
        role (UserRole): The role of the user.
        created_at (datetime): The timestamp of when the user was created.
        updated_at (datetime): The timestamp of when the user was
            last updated.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserRole.ADMIN, UserRole.VOTER), nullable=False, default=UserRole.VOTER)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    def __repr__(self):
        return f'<User {self.username}>'
