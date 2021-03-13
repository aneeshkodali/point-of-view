# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class HandModel(BaseMixin, Document):
    '''
    Hands
    '''

    hand_id = IntField(primary_key=True)
    hand = StringField()

    meta = {'collection': 'hands'}
  
