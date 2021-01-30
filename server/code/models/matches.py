from mongoengine import UUIDField, URLField, DateTimeField, IntField, StringField, ReferenceField
import datetime
from uuid import uuid4

from models.base import BaseModel
from models.rounds import RoundModel
from models.tournaments import TournamentModel

class MatchModel(BaseModel):
    '''
    Matches
    '''
#, default='dda2c34f-f992-4701-a76e-e02b12cbdf0e'
    match_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    name = StringField(default="")
    date = DateTimeField(default=datetime.datetime(1700, 1, 1))
    tournament_id = ReferenceField(TournamentModel)
    round_id = ReferenceField(RoundModel, default=0)
    score = StringField(default="")
    sets = IntField(default=0)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'matches'}

    @classmethod
    def find_by_link(cls, link):
        return MatchModel.objects(link=link).first()
