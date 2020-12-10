from db import db

class PointModel(db.EmbeddedDocument):

    server = db.StringField()
    receiver = db.StringField()
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