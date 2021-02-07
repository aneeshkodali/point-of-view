from mongoengine import StringField, IntField, DateTimeField, URLField, ReferenceField
from mongoengine.queryset.visitor import Q

from models.base import BaseModel
from models.default_values import default_uuid_value, default_date_value, default_year_value
from models.genders import GenderModel
from models.levels import LevelModel
from models.surfaces import SurfaceModel
from models.tournament_names import TournamentNameModel

class TournamentModel(BaseModel):
    '''
    Tournaments - each record is a unique combination of (tournament_name_id, gender_id, year)
    '''
    
    tournament_id = StringField(primary_key=True, default=default_uuid_value)
    tournament_name_id = ReferenceField(TournamentNameModel)
    year = IntField(default=default_year_value)
    gender_id = ReferenceField(GenderModel, default=0)
    date = DateTimeField(default=default_date_value)
    size = IntField(default=0)
    points = IntField(default=0)
    sets = IntField(default=0)
    surface_id = ReferenceField(SurfaceModel, default=0)
    level_id = ReferenceField(LevelModel, default=0)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'tournaments'}

    def json(self):
        return {
            'tournament_id': self.tournament_id,
            'name': self.tournament_name_id.name,
            'year': self.year,
            'gender': self.gender_id.gender,
            'date': self.date,
            'size': self.size,
            'points': self.points,
            'sets': self.sets,
            'surface': self.surface_id.surface,
            'level_id': self.level_id.level,
            'link': self.link
        }

    @classmethod
    def find_by_link(cls, link):
        return TournamentModel.objects(link=link)

    @classmethod
    def find_by_name_id_and_gender_id_and_year(cls, tournament_name_id, gender_id, year):
        return TournamentModel.objects(Q(tournament_name_id=tournament_name_id) & Q(gender_id=gender_id) & Q(year=year)).first()



