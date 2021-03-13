# python imports
from mongoengine import Document, StringField, IntField, DateField, URLField

# project imports
from models.shared.base_mixin import BaseMixin
from models.default_values import default_uuid_value, default_date_value, default_year_value, default_tournament_name_id_value

class TournamentModel(BaseMixin, Document):
    '''
    Tournaments - each record is a unique combination of (tournament_name_id, gender_id, year)
    '''
    
    tournament_id = StringField(primary_key=True, default=default_uuid_value)
    tournament_name_id = StringField(required=True, default=default_tournament_name_id_value)
    year = IntField(default=default_year_value)
    gender_id = IntField(required=True)
    date = DateField(default=default_date_value)
    size = IntField(default=0)
    points = IntField(default=0)
    sets = IntField(default=0)
    surface_id = IntField(required=True)
    level_id = IntField(required=True)
    link = URLField(unique=True, nullable=False)

    meta = {'collection': 'tournaments'}
