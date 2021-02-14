from mongoengine import StringField, IntField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.sets import SetModel
from models.players import PlayerModel

class SetPlayerModel(BaseModel):
    '''
    Each row is a set /player
    So a set should have 2 rows, one for each player
    '''

    set_player_id = StringField(primary_key=True, default=default_uuid_value)
    match_set = ReferenceField(SetModel)
    player = ReferenceField(PlayerModel)
    score = IntField()
    win = IntField(default=0)

    meta = {'collection': 'match_sets'}

    def json(self):
        return {
            'match_player_id': self.set_player_id,
            'match_set': self.match_set,
            'player': self.player,
            'score': self.score,
            'win': self.win
        }
