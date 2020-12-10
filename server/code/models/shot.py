from db import db
from player import PlayerModel

class ShotModel(db.EmbeddedDocument):

    shot_number = db.IntField()
    shot_number_w_serve = db.IntField()
    shot_by = db.ReferenceField(PlayerModel)
    shot = db.StringField()
    location = db.StringField()
    result = db.StringField()