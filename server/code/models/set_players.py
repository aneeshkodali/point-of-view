# python imports
from mongoengine import Document, StringField, IntField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class SetPlayerModel(BaseMixin, Document):
    '''
    Each row is a set /player
    So a set should have 2 rows, one for each player
    '''

    set_player_id = StringField(primary_key=True, default=default_uuid_value)
    set_id = StringField(required=True)
    player_id = StringField(required=True)
    score = IntField()
    win = IntField(default=0)

    meta = {'collection': 'set_players'}

