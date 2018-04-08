from datetime import datetime
from . import db, ma
from .modelBase import Base


class ChangeRequest(db.Model, Base):
    __tablename__ = 'change_requests'
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    changeType = db.Column(db.String(6), index=True)  # create/update/delete
    content = db.Column(db.Text)

    # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', lazy=True)

    def __repr__(self):
        return '<ChangeRequest(entity="{}", user_id="{}">'.format(self.entity,
                                                                  self.user_id)

    def __str__(self):
        return repr(self)


class ChangeRequestSchema(ma.ModelSchema):
    class Meta:
        model = ChangeRequest
