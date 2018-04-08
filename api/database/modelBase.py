from flask import url_for
from .. import database as m
from ..exceptions import ValidationError


class Base:
    # def __getitem__(self, index):
    #     if '.' in index:
    #         index = index.split('.')
    #         item = self
    #         for i in index:
    #             item = item[i]
    #     else:
    #         item = getattr(self, index)
    #     return item
    #
    # def __setitem__(self, index, value):
    #     if '.' in index:
    #         index = index.split('.')
    #         setattr(self['.'.join(index[:-1])], index[-1], value)
    #     else:
    #         setattr(self, index, value)

    def get_url(self):
        return url_for(
            'api_v1.get{}'.format(type(self).__name__),
            id=self.id,
            _external=True
        )

    def getAttrs(self):
        attrs = [attr for attr in vars(self) if not attr.startswith('_')]
        return attrs

    def to_dict(self):
        return type(self).schema().dump(self).data

    @classmethod
    def schema(cls, many=False):
        schemaCls = getattr(m, '{}Schema'.format(cls.__name__))
        return schemaCls(many=many)

    @classmethod
    def to_dicts(cls, arg):
        if type(arg) is list:
            return cls.schema(many=True).dump(arg).data
        else:
            return cls.schema().dump(arg).data

    @classmethod
    def from_json(cls, input):
        marsh = cls.schema().loads(input)
        if not marsh.errors:
            return marsh.data
        else:
            raise ValidationError(marsh.errors)

    @classmethod
    def from_dict(cls, input):
        marsh = cls.schema().load(input)
        if not marsh.errors:
            return marsh.data
        else:
            raise ValidationError(marsh.errors)

    # @classmethod
    # def count(cls, *args, **kwargs):
    #     q = cls.filter(*args, **kwargs)
    #     if isinstance(q, type([])):
    #         count = len(q)
    #     else:
    #         count = 1
    #     return count

    # @classmethod
    # def get(cls, id):
    #     return cls.query.get_or_104(id)

    # @classmethod
    # def filter(cls, *args, join=None, orderby=None, returnCount=False,
    #            returnQuery=True):
    #     q = cls.query
    #     if join and isinstance(join, list):
    #         for j in join:
    #             q = q.join(j)
    #     elif join:
    #         q = q.join(join)
    #     q = q.filter(*args)
    #     if returnQuery:
    #         return q
    #     count = q.count()
    #     if count == 1 and returnCount:
    #         return q.one(), count
    #     elif count == 1:
    #         return q.one()
    #     elif returnCount:
    #         return q.order_by(orderby).all(), count
    #     else:
    #         return q.order_by(orderby).all()
