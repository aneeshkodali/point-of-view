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

    @classmethod
    def find_by_tournament_name(cls, tournament_name):
        return TournamentNameModel.objects(tournament_name=tournament_name).first()
