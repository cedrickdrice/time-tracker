from app import db
from datetime import datetime


class User(db.Model):
    """ Class User : data model for handling user query """
    
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(64), index=True, unique=True, nullable=False)
    email = db.Column('email', db.String(80), index=True, unique=True, nullable=False)
    password = db.Column('password', db.String(500), nullable=False)
    created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)

    # serialize data to json
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        }
