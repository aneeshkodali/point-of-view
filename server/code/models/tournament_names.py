# python imports
from mongoengine import Document, StringField

# project imports
from models.default_values import default_uuid_value
from models.shared.base_mixin import BaseMixin

class TournamentNameModel(BaseMixin, Document):
    '''
    Tournament Names
    '''

    tournament_name_id = StringField(primary_key=True, default=default_uuid_value)
    tournament_name = StringField()

    meta = {'collection': 'tournament_names'}
