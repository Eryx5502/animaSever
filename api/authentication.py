from flask import g
from flask_httpauth import HTTPBasicAuth
from .database import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verifyAuthToken(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verifyPassword(password):
            return False
        g.authWithPassword = True  # Store auth mode for token generation
    else:
        g.authWithPassword = False
    g.user = user
    return True
