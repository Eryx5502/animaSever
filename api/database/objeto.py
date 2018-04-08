from . import db, ma
from .modelBase import Base


class Objeto(db.Model, Base):
    __tablename__ = 'objetos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), index=True, nullable=False, unique=True)
    info = db.Column(db.String(50))
    presencia = db.Column(db.Integer)
    calidad = db.Column(db.Integer)
    esArtefacto = db.Column(db.Boolean)
    precio = db.Column(db.String(10))
    disponibilidad = db.Column(db.String(10))
    arma_id = db.Column(db.Integer, db.ForeignKey('armas.id'))
    armadura_id = db.Column(db.Integer, db.ForeignKey('armaduras.id'))

    armaBase = db.relationship('Arma', lazy=True)
    armaduraBase = db.relationship('Armadura', lazy=True)

    def __repr__(self):
        return '<Objeto(Nombre="{}", arma="{}", armadura="{}")>'. \
                                                    format(self.nombre,
                                                           self.armaBase,
                                                           self.armaduraBase)


class ObjetoSchema(ma.ModelSchema):
    class Meta:
        model = Objeto
