# python imports
from mongoengine import Document, IntField

# project imports
from models.shared.base_mixin import BaseMixin

class BackhandModel(BaseMixin, Document):
    '''
    Backhands
    '''

    backhand_id = IntField(primary_key=True)
    backhand = IntField()

    meta = {'collection': 'backhands'}
