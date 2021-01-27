from mongoengine import UUIDField, IntField
from mongoengine.queryset.visitor import Q

from models.base import BaseModel

class MatchPlayerModel(BaseModel):
    '''
    Each row is a match id/player id/did player win
    So a match should have 2 rows, one for each player
    '''

    match_id = UUIDField(required=True)
    player_id = UUIDField(required=True)
    win = IntField()

    meta = {'collection': 'match_players'}

    @classmethod
    def find_by_match_id_and_player_id(cls, match_id, player_id):
        return MatchPlayerModel.objects(Q(match_id=match_id) & Q(player_id=player_id)).first()