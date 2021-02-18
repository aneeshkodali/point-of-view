from mongoengine import StringField, IntField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.games import GameModel
from models.players import PlayerModel

class GamePlayerModel(BaseModel):
    '''
    Each row is a game /player
    So a set should have 2 rows, one for each player
    '''

    game_player_id = StringField(primary_key=True, default=default_uuid_value)
    game = ReferenceField(GameModel)
    player = ReferenceField(PlayerModel)
    score = IntField()
    serve = IntField()
    win = IntField()

    meta = {'collection': 'game_players'}

    def json(self):
        return {
            'game_player_id': self.game_player_id,
            'game': self.game,
            'player': self.player,
            'score': self.score,
            'serve': self.serve,
            'win': self.win
        }
