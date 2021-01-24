from mongoengine import IntField, StringField

from models.base import BaseModel

class LevelModel(BaseModel):
    '''
    Tournament levels
    '''

    level_id = IntField(primary_key=True)
    level = StringField()

    meta = {'collection': 'levels'}

    @classmethod
    def find_by_level(cls, level):
        return LevelModel.objects(level=level).first()