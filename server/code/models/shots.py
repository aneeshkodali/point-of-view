from mongoengine import IntField, StringField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.players import PlayerModel
from models.points import PointModel

class ShotModel(BaseModel):
    '''
    Shots
    '''

    shot_id = StringField(primary_key=True, default=default_uuid_value)
    point = ReferenceField(PointModel)
    shot_number = IntField()
    shot_number_w_serve = IntField()
    shot_by = ReferenceField(PlayerModel)
    shot = StringField()
    location = StringField()
    result = StringField()

    meta = {'collection': 'shots'}
