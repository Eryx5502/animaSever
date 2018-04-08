from . import db, ma
from .modelBase import Base


class Ventaja(db.Model, Base):
    __tablename__ = 'ventajas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), index=True, nullable=False, unique=True)
    descripcion = db.Column(db.String, index=True)
    limitaciones = db.Column(db.String)
    coste = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Ventaja ({})>'.format(self.nombre)

    def __str__(self):
        return '{} [{}]'.format(self.nombre, self.coste)


class VentajaSchema(ma.ModelSchema):
    class Meta:
        model = Ventaja
