from mongoengine import IntField, StringField
from models.base import BaseModel

class LevelModel(BaseModel):
    '''
    Tournament levels
    '''

    level_id = IntField(primary_key=True)
    abbreviation = StringField()
    level = StringField()

    meta = {'collection': 'levels'}

    @classmethod
    def find_by_abbreviation(cls, abbreviation):
        return LevelModel.objects(abbreviation=abbreviation).first()

    @classmethod
    def find_by_round(cls, level):
        return LevelModel.objects(level=level).first()