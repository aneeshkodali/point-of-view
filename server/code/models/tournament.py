from db import db

class TournamentModel(db.Document):

    link = db.URLField()
    name = db.StringField()
    surface = db.StringField(choices=['Hard', 'Clay', 'Grass', 'Carpet', 'None'], default='None')
    gender = db.StringField(min_length=1, max_length=1, default='U')
    sets = db.IntField(max_value=5, default=0)