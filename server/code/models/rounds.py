from mongoengine import IntField, StringField

from models.base import BaseModel

class RoundModel(BaseModel):
    '''
    Match rounds
    '''

    round_id = IntField(primary_key=True)
    round_name = StringField()

    meta = {'collection': 'rounds'}

    @classmethod
    def find_by_round(cls, round_name):
        return RoundModel.objects(round_name=round_name).first()