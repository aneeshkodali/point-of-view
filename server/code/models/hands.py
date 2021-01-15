from db import db
import json

class HandModel(db.Document):
    '''
    Hand that the player plays with (right or left)
    '''

    hand_id = db.IntField(primary_key=True)
    abbreviation = db.StringField()
    hand = db.StringField()

    meta = {'collection': 'hands'}

    def json(self):
        return json.loads(self.to_json())

    @classmethod
    def find_by_hand_id(cls, hand_id):
        return HandModel.objects(hand_id=hand_id).first()
    
    @classmethod
    def find_by_abbreviation(cls, abbreviation):
        return HandModel.objects(abbreviation=abbreviation).first()

    @classmethod
    def find_by_hand(cls, hand):
        return HandModel.objects(hand=hand).first()