from flask import request, g
from flask_restful import Resource
from ..authentication import auth
from ..decorators import collection
from ..database import db, ChangeRequest
from ..exceptions import ValidationError


class DBCollection(Resource):
    """ Class implementing the API for accessing collections from animadb """
    # Define a dict of searchable entities
    def __init__(self, entity):
        self.entity = entity
        self.method_decorators = {
            'get': [collection(entity)],
            'post': [auth.login_required]
        }

    def entityName(self):
        return self.entity.__name__

    def get(self):
        return self.entity.query

    def post(self):
        if not request.json:
            raise ValidationError('No JSON in request')
        object = self.entity.from_dict(request.json)
        if g.user.isAdmin():
            db.session.add(object)
            db.session.commit()
        else:
            changeRequest = ChangeRequest(
                entity=self.entityName(),
                changeType="create",
                content=str(request.json)
            )
            changeRequest.user = g.user
            db.session.add(changeRequest)
            db.session.commit()

        return {}, 201


class DBObject(Resource):
    """ Class implementing the API for accessing objects from animadb """
    def __init__(self, entity):
        self.entity = entity
        self.decorators = {
            'post': [auth.login_required],
            'put': [auth.login_required],
            'delete': [auth.login_required]
        }

    def entityName(self):
        return self.entity.__name__

    def get(self, id):
        return self.entity.query.get_or_404(id).to_dict()
