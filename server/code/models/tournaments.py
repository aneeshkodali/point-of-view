from mongoengine import UUIDField, StringField, IntField, DateTimeField, URLField
from mongoengine.queryset.visitor import Q
import datetime
from uuid import uuid4

from models.base import BaseModel

class TournamentModel(BaseModel):
    '''
    Tournaments - each record is a unique combination of (tournament_name_id, gender_id, year)
    '''
    
    tournament_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    tournament_name_id = UUIDField(binary=False, default='4e1f7f4b-6f3e-43ce-954d-aa9cf6ca52e4')
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
    def find_by_name_id_and_gender_id_and_year(cls, tournament_name_id, gender_id, year):
        return TournamentModel.objects(Q(tournament_name_id=tournament_name_id) & Q(gender_id=gender_id) & Q(year=year)).first()



