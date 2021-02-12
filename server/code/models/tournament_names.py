from mongoengine import StringField

from models.base import BaseModel
from models.default_values import default_uuid_value

class TournamentNameModel(BaseModel):
    '''
    Tournament Names
    '''

    tournament_name_id = StringField(primary_key=True, default=default_uuid_value)
    tournament_name = StringField()

    meta = {'collection': 'tournament_names'}
