# python imports
from mongoengine import Document, StringField, IntField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class GamePlayerModel(BaseMixin, Document):
    '''
    Each row is a game /player
    So a game should have 2 rows, one for each player
    '''

    game_player_id = StringField(primary_key=True, default=default_uuid_value)
    game_id = StringField(required=True)
    player_id = StringField(required=True)
    score = IntField()
    serve = IntField()
    win = IntField()

    meta = {'collection': 'game_players'}