from mongoengine import StringField, IntField, ReferenceField
from mongoengine.queryset.visitor import Q

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.matches import MatchModel
from models.players import PlayerModel

class MatchPlayerModel(BaseModel):
    '''
    Each row is a match id/player id/did player win
    So a match should have 2 rows, one for each player
    '''

    match_player_id = StringField(primary_key=True, default=default_uuid_value)
    match = ReferenceField(MatchModel)
    player = ReferenceField(PlayerModel)
    win = IntField(default=0)

    meta = {'collection': 'match_players'}

    def json(self):
        return {
            'match_player_id': self.match_player_id,
            'match': self.match,
            'player': self.player,
            'win': self.win
        }

    @classmethod
    def find_by_match_and_player(cls, match, player):
        return MatchPlayerModel.objects(Q(match=match) & Q(player=player)).first()