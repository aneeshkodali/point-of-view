# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class LevelModel(BaseMixin, Document):
    '''
    Tournament levels
    '''

    level_id = IntField(primary_key=True)
    level = StringField()

    meta = {'collection': 'levels'}
