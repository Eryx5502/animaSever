from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


from .arma import Arma
from .armadura import Armadura
from .hechizo import Hechizo
from .objeto import Objeto
from .poderPsiquico import PoderPsiquico
from .ventaja import Ventaja
from .user import User
from .changeRequest import ChangeRequest
