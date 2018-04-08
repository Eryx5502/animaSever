from flask import g
from flask_restful import Resource
from ..authentication import auth


class AuthTokenAPI(Resource):
    method_decorators = [auth.login_required]

    def get(self):
        if g.authWithPassword:
            token = g.user.generateAuthToken()
            return {'token': token.decode('ascii')}
        else:
            return {'error': 'Permission denied'}, 403
