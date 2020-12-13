from db import db
from player import PlayerModel
from shot import ShotModel

class PointModel(db.EmbeddedDocument):
    
    point_number = db.IntField()
    server = db.ReferenceField(PlayerModel)
    receiver = db.ReferenceField(PlayerModel)
    set_score = db.StringField()
    set_score_server = db.IntField()
    set_score_receiver = db.IntField()
    set_in_match = db.IntField()
    game_score = db.StringField()
    game_score_server = db.IntField()
    game_score_receiver = db.IntField()
    game_in_set = db.IntField()
    point_score = db.StringField()
    point_score_server = db.IntField()
    point_score_receiver = db.IntField()
    point_in_game = db.IntField()
    side = db.StringField()
    num_shots = db.IntField()
    rally_length = db.IntField()
    result = db.StringField()
    winner = db.ReferenceField(PlayerModel)
    loser = db.ReferenceField(PlayerModel)
    shots = db.EmbeddedDocumentListField(ShotModel, default=[])