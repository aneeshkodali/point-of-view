# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class RoundModel(BaseMixin, Document):
    '''
    Match rounds
    '''

    round_id = IntField(primary_key=True)
    round_name = StringField()

    meta = {'collection': 'rounds'}
