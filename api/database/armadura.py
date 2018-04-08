from . import db, ma
from .modelBase import Base


class Armadura(db.Model, Base):
    __tablename__ = 'armaduras'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), index=True, unique=True)
    fil = db.Column(db.Integer)
    con = db.Column(db.Integer)
    pen = db.Column(db.Integer)
    cal = db.Column(db.Integer)
    ele = db.Column(db.Integer)
    fri = db.Column(db.Integer)
    ene = db.Column(db.Integer)
    reqArmadura = db.Column(db.Integer)
    naturalPen = db.Column(db.Integer)
    resMovimiento = db.Column(db.Integer)
    entereza = db.Column(db.Integer)
    clase = db.Column(db.String(15))
    localizacion = db.Column(db.String(15))
    presencia = db.Column(db.Integer)

    def __repr__(self):
        return '<Objeto(Nombre="{}", clase="{}", localización="{}">'. \
                                                    format(self.nombre,
                                                           self.clase,
                                                           self.localizacion)

    def __str__(self):
        return self.nombre


class ArmaduraSchema(ma.ModelSchema):
    class Meta:
        model = Armadura
