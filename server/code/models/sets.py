# python imports
from mongoengine import IntField, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseModel

class SetModel(BaseModel):
    '''
    Sets
    '''

    set_id = StringField(primary_key=True, default=default_uuid_value)
    match_id = StringField(required=True)
    set_in_match = IntField(default=0)
    score = StringField()

    meta = {'collection': 'sets'}
