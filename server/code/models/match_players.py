from mongoengine import UUIDField, IntField, ReferenceField
from mongoengine.queryset.visitor import Q
from uuid import uuid4

from models.base import BaseModel
from models.matches import MatchModel
from models.players import PlayerModel

class MatchPlayerModel(BaseModel):
    '''
    Each row is a match id/player id/did player win
    So a match should have 2 rows, one for each player
    '''

    match_player_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    match_id = ReferenceField(MatchModel)
    player_id = ReferenceField(PlayerModel)
    win = IntField(default=0)

    meta = {'collection': 'match_players'}

    @classmethod
    def find_by_match_id_and_player_id(cls, match_id, player_id):
        return MatchPlayerModel.objects(Q(match_id=match_id) & Q(player_id=player_id)).first()