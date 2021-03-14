# python imports
from mongoengine import Document, StringField, IntField

from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class MatchPlayerModel(BaseMixin, Document):
    '''
    Each row is a match id/player id/did player win
    So a match should have 2 rows, one for each player
    '''

    match_player_id = StringField(primary_key=True, default=default_uuid_value)
    match_id = StringField(required=True)
    player_id = StringField(required=True)
    win = IntField()

    meta = {'collection': 'match_players'}
