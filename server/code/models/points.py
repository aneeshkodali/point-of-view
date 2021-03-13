# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class PointModel(BaseMixin, Document):
    '''
    Points
    '''

    point_id = StringField(primary_key=True, default=default_uuid_value)
    game_id = StringField(required=True)
    point_in_game = IntField(default=0)
    point_in_set = IntField(default=0)
    point_in_match = IntField(default=0)
    number_of_shots = IntField()
    rally_length =  IntField()
    result = StringField()
    side_id = StringField(required=True)
    score = StringField()

    meta = {'collection': 'points'}

