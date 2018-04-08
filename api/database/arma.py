from . import db, ma
from .modelBase import Base


class Arma(db.Model, Base):
    __tablename__ = 'armas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), index=True, unique=True)
    danyo = db.Column(db.Integer)
    velocidad = db.Column(db.Integer)
    fuerza1mano = db.Column(db.Integer)
    fuerza2manos = db.Column(db.Integer)
    critico1 = db.Column(db.String(3))
    critico2 = db.Column(db.String(3))
    especial = db.Column(db.String(40))
    entereza = db.Column(db.Integer)
    rotura = db.Column(db.Integer)
    presencia = db.Column(db.Integer)
    tipo1 = db.Column(db.String(20))
    tipo2 = db.Column(db.String(20))
    bonoParada = db.Column(db.Integer)
    bonoEsquiva = db.Column(db.Integer)
    cadencia = db.Column(db.Integer)
    recarga = db.Column(db.Integer)
    alcance = db.Column(db.Integer)
    fuerza = db.Column(db.Integer)

    def __repr__(self):
        return '<Arma(Nombre="{}", tipo1="{}", tipo2="{}">'. \
                                                    format(self.nombre,
                                                           self.tipo1,
                                                           self.tipo2)

    def __str__(self):
        return self.nombre


class ArmaSchema(ma.ModelSchema):
    class Meta:
        model = Arma
