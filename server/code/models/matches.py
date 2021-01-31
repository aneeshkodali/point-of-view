from mongoengine import URLField, DateTimeField, IntField, StringField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value, default_date_value
from models.rounds import RoundModel
from models.tournaments import TournamentModel

class MatchModel(BaseModel):
    '''
    Matches
    '''
    match_id = StringField(primary_key=True, default=default_uuid_value)
    name = StringField(default="")
    date = DateTimeField(default=default_date_value)
    tournament_id = ReferenceField(TournamentModel)
    round_id = ReferenceField(RoundModel, default=0)
    score = StringField(default="")
    sets = IntField(default=0)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'matches'}

    @classmethod
    def find_by_link(cls, link):
        return MatchModel.objects(link=link).first()
