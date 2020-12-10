import datetime
from db import db
from tournament import TournamentModel
from player import PlayerModel
from point import PointModel

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