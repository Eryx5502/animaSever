from . import db, ma
from .modelBase import Base


class Hechizo(db.Model, Base):
    __tablename__ = 'hechizos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), index=True, nullable=False, unique=True)
    nivel = db.Column(db.Integer)
    via = db.Column(db.String(20), index=True)
    accion = db.Column(db.String(6))
    tipo = db.Column(db.String(15))
    efectos = db.Column(db.String, index=True)

    intBase = db.Column(db.String(2))
    intIntermedio = db.Column(db.String(2))
    intAvanzado = db.Column(db.String(2))
    intArcano = db.Column(db.String(2))

    zeonBase = db.Column(db.String(5))
    zeonIntermedio = db.Column(db.String(5))
    zeonAvanzado = db.Column(db.String(5))
    zeonArcano = db.Column(db.String(5))

    mantDiario = db.Column(db.Boolean)
    mantBase = db.Column(db.Integer)
    mantIntermedio = db.Column(db.Integer)
    mantAvanzado = db.Column(db.Integer)
    mantArcano = db.Column(db.Integer)

    base = db.Column(db.String(50))
    intermedio = db.Column(db.String(50))
    avanzado = db.Column(db.String(50))
    arcano = db.Column(db.String(50))

    def __repr__(self):
        s = '<Hechizo(vía="{}", nivel="{}", nombre="{}")>'.format(self.via,
                                                                  self.nivel,
                                                                  self.nombre)
        return s

    def __str__(self):
        return '{}, {}, {}'.format(self.nombre, self.via, self.nivel)


class HechizoSchema(ma.ModelSchema):
    class Meta:
        model = Hechizo
