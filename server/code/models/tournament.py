from mongoengine.queryset.visitor import Q
import json
from db import db

class TournamentModel(db.Document):

    link = db.URLField()
    name = db.StringField()
    surface = db.StringField(choices=['Hard', 'Clay', 'Grass', 'Carpet', 'None'], default='None')
    gender = db.StringField(min_length=1, max_length=1, default='U')
    sets = db.IntField(max_value=5, default=0)

    meta = {'collection': 'tournaments'}

    def json(self):
            return json.loads(self.to_json())

    @classmethod
    def find_by_name_and_gender(cls, name, gender):
        return TournamentModel.objects(Q(name=name) & Q(gender=gender)).first()

