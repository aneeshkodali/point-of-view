# python imports
from mongoengine import Document, URLField, DateField, IntField, StringField

# project imports
from models.default_values import default_uuid_value, default_date_value
from models.shared.base_mixin import BaseMixin

class MatchModel(BaseMixin, Document):
    '''
    Matches
    '''
    match_id = StringField(primary_key=True, default=default_uuid_value)
    name = StringField(default="")
    date = DateField(default=default_date_value)
    tournament_id = StringField(required=True)
    round_id = IntField(required=True)
    sets = IntField(default=0)
    suffix = StringField(unique=True, nullable=False)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'matches'}
