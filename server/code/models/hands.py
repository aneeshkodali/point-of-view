from mongoengine import IntField, StringField

from models.base import BaseModel

class HandModel(BaseModel):
    '''
    Hand that the player plays with
    '''

    hand_id = IntField(primary_key=True)
    hand = StringField()

    meta = {'collection': 'hands'}
  
    @classmethod
    def find_by_hand(cls, hand):
        return HandModel.objects(hand=hand).first()