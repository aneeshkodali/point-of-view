# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class ShotModel(BaseMixin, Document):
    '''
    Shots
    '''

    shot_id = StringField(primary_key=True, default=default_uuid_value)
    point_id = StringField(required=True)
    shot_number = IntField()
    shot_number_w_serve = IntField()
    shot_by = StringField(required=True)
    shot = StringField()
    location = StringField()
    result = StringField()

    meta = {'collection': 'shots'}
