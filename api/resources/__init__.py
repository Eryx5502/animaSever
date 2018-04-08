from flask import Blueprint
from flask_restful import Api
from ..database import Arma, Armadura, Hechizo, Objeto, PoderPsiquico, Ventaja
from .animadb import DBCollection, DBObject
from .authToken import AuthTokenAPI
from ..exceptions import bad_request, ValidationError

resources_bp = Blueprint('resources', __name__)
api = Api(resources_bp)


# Add get-Token resource
api.add_resource(AuthTokenAPI, '/get-token', endpoint='authTokenAPI')
# Add resources for accessing animadb collections and objects
# dict of resources and
entities = [Arma, Armadura, Hechizo, Objeto, PoderPsiquico, Ventaja]
for entity in entities:
    api.add_resource(
        DBCollection,
        '/animadb/{}'.format(entity.__tablename__),
        endpoint='get{}'.format(entity.__tablename__),
        resource_class_args=(entity,)
    )
    api.add_resource(
        DBObject,
        '/animadb/{}/<int:id>'.format(entity.__tablename__),
        endpoint="get{}".format(entity.__name__),
        resource_class_args=(entity,)
    )


@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.dict)
