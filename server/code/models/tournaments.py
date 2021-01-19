from mongoengine import UUIDField, StringField, IntField, DateTimeField, URLField
from mongoengine.queryset.visitor import Q
import datetime
from uuid import uuid4

from models.base import BaseModel

class TournamentModel(BaseModel):
    '''
    Tournaments - each record is a unique combination of (tournament, gender, year)
    '''

    #tournament_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    name = StringField()
    year = IntField(default=2300)
    gender_id = IntField(default=0)
    date = DateTimeField(default=datetime.datetime(1700, 1, 1))
    size = IntField(default=0)
    points = IntField(default=0)
    sets = IntField(default=0)
    surface_id = IntField(default=0)
    level_id = IntField(default=0)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'tournaments'}

    @classmethod
    def find_by_id_and_gender_and_year(cls, tournament_id, gender, year):
        return TournamentModel.objects(Q(tournament_id=tournament_id) & Q(gender=gender) & Q(year=year)).first()



