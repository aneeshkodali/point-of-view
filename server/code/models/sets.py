# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class SetModel(BaseMixin, Document):
    '''
    Sets
    '''

    set_id = StringField(primary_key=True, default=default_uuid_value)
    match_id = StringField(required=True)
    set_in_match = IntField(default=0)

    meta = {'collection': 'sets'}
