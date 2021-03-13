# python imports
from mongoengine import Document, StringField, IntField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class PointPlayerModel(BaseMixin, Document):
    '''
    Each row is a point /player
    So a point should have 2 rows, one for each player
    '''

    point_player_id = StringField(primary_key=True, default=default_uuid_value)
    point_id = StringField(required=True)
    player_id = StringField(required=True)
    score = StringField()
    serve = IntField()
    win = IntField()

    meta = {'collection': 'point_players'}

