from flask import Flask
from config import Config
# from flask_restful import Api
from .database import db, migrate, ma


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .resources import resources_bp
    app.register_blueprint(resources_bp)  # , url_prefix='/v1')

    return app

# api = Api(app)
# auth = HTTPBasicAuth()


# from .authentication import verify_password
# from .pagination import paginate
# from . import database, resources, exceptions
