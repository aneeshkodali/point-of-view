from mongoengine import StringField, IntField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.points import PointModel
from models.players import PlayerModel

class PointPlayerModel(BaseModel):
    '''
    Each row is a point /player
    So a point should have 2 rows, one for each player
    '''

    point_player_id = StringField(primary_key=True, default=default_uuid_value)
    point = ReferenceField(PointModel)
    player = ReferenceField(PlayerModel)
    score = StringField()
    serve = IntField()
    win = IntField()

    meta = {'collection': 'point_players'}

    def json(self):
        return {
            'point_player_id': self.point_player_id,
            'point': self.point,
            'player': self.player,
            'score': self.score,
            'serve': self.serve,
            'win': self.win
        }
