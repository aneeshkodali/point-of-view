import datetime
from db import db
import json
from models.tournament import TournamentModel
from models.player import PlayerModel
from models.point import PointModel

class MatchModel(db.Document):

    link = db.URLField(unique=True, required=True)
    match_date = db.DateTimeField(default=datetime.datetime(1900, 1, 1))
    gender = db.StringField(min_length=1, max_length=1, default='U')
    tournament = db.ReferenceField(TournamentModel)
    match_round = db.StringField(default='NONE')
    players = db.ListField(db.ReferenceField(PlayerModel))
    title = db.StringField(default='None')
    result = db.StringField(default='None')
    winner = db.ReferenceField(PlayerModel, default='None')
    loser = db.ReferenceField(PlayerModel, default='None')
    score = db.StringField(default='None')
    sets = db.IntField(max_value=5, default=0)
    points = db.EmbeddedDocumentListField(PointModel, default=[])

    meta = {'collection': 'matches'}

    def json(self):
            return json.loads(self.to_json())

    @classmethod
    def find_by_link(cls, link):
        return MatchModel.objects(link=link).first()