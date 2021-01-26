from mongoengine import UUIDField, URLField, DateTimeField, IntField, StringField
import datetime

from models.base import BaseModel

class MatchModel(BaseModel):
    '''
    Matches
    '''

    match_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    name = StringField(default="")
    date = DateTimeField(default=datetime.datetime(1700, 1, 1))
    tournament_id = UUIDField(binary=False, default='dda2c34f-f992-4701-a76e-e02b12cbdf0e')
    round_id = IntField(default=0)
    score = StringField(default="")
    sets = IntField(default=0)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'matches'}

    @classmethod
    def find_by_link(cls, link):
        return MatchModel.objects(link=link).first()
