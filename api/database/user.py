from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer,
                          BadSignature, SignatureExpired)
from flask import current_app
from . import db, ma
from .modelBase import Base


class User(db.Model, Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(40), index=True, unique=True)
    hash_password = db.Column(db.String(128))
    role = db.Column(db.String(10))

    def __repr__(self):
        return '<User(username="{}", email="{}">'.format(self.username,
                                                         self.email)

    def __str__(self):
        return self.nombre

    def setPassword(self, password):
        self.hash_password = generate_password_hash(password)

    def verifyPassword(self, password):
        return check_password_hash(self.hash_password, password)

    def generateAuthToken(self, expiration=18000):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    def isAdmin(self):
        if self.role == 'admin':
            return True
        else:
            return False

    @staticmethod
    def verifyAuthToken(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
