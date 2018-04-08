from . import db, ma
from .modelBase import Base


class PoderPsiquico(db.Model, Base):
    __tablename__ = 'poderesPsiquicos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), index=True, nullable=False)
    disciplina = db.Column(db.String(20), index=True)
    nivel = db.Column(db.Integer)
    mantenido = db.Column(db.Boolean)
    accion = db.Column(db.String(6))
    efectos = db.Column(db.String, index=True)

    rutinario = db.Column(db.String(20))
    facil = db.Column(db.String(20))
    medio = db.Column(db.String(20))
    dificil = db.Column(db.String(20))
    muyDificil = db.Column(db.String(20))
    absurdo = db.Column(db.String(20))
    casiImposible = db.Column(db.String(20))
    imposible = db.Column(db.String(20))
    inhumano = db.Column(db.String(20))
    zen = db.Column(db.String(20))

    def __repr__(self):
        return '<Poder psíquico(disciplina="{}", nivel="{}", nombre="{}")>'. \
                                                        format(self.disciplina,
                                                               self.nivel,
                                                               self.nombre)

    def __str__(self):
        return '{}, {}, {}'.format(self.nombre, self.disciplina, self.nivel)


class PoderPsiquicoSchema(ma.ModelSchema):
    class Meta:
        model = PoderPsiquico
