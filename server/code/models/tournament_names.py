from mongoengine import UUIDField, StringField
from uuid import uuid4

from models.base import BaseModel

class TournamentNameModel(BaseModel):
    '''
    Tournament Names
    '''

    tournament_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    name = StringField()

    meta = {'collection': 'tournament_names'}

    @classmethod
    def find_by_name(cls, name):
        return TournamentNameModel.objects(name=name).first()
