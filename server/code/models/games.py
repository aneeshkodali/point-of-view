# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class GameModel(BaseMixin, Document):
    '''
    Games
    '''

    game_id = StringField(primary_key=True, default=default_uuid_value)
    set_id = StringField(required=True)
    game_in_set = IntField(default=0)
    game_in_match = IntField(default=0)
    score = StringField()

    meta = {'collection': 'games'}
