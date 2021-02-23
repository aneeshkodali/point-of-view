from mongoengine import IntField, StringField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.games import GameModel
from models.sides import SideModel

class PointModel(BaseModel):
    '''
    Points
    '''

    point_id = StringField(primary_key=True, default=default_uuid_value)
    game = ReferenceField(GameModel)
    point_in_game = IntField(default=0)
    point_in_set = IntField(default=0)
    point_in_match = IntField(default=0)
    side = ReferenceField(SideModel)
    score = StringField()

    meta = {'collection': 'points'}

    def json(self):
        return {
            'point_id': self.point_id,
            'game': self.game,
            'point_in_game': self.point_in_game,
            'point_in_set': self.point_in_set,
            'point_in_match': self.point_in_match,
            'side': self.side,
            'score': self.score
        }

