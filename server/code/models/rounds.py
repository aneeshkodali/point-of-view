from mongoengine import IntField, StringField
from models.base import BaseModel

class RoundModel(BaseModel):
    '''
    Match rounds
    '''

    round_id = IntField(primary_key=True)
    abbreviation = StringField()
    round_name = StringField()

    meta = {'collection': 'rounds'}

    @classmethod
    def find_by_abbreviation(cls, abbreviation):
        return HandModel.objects(abbreviation=abbreviation).first()

    @classmethod
    def find_by_round(cls, round_name):
        return HandModel.objects(round_name=round_name).first()