import datetime
from db import db

class PlayerModel(db.Document):

    link = db.URLField(unique=True, required=True)
    gender = db.StringField(min_length=1, max_length=1, default='U')
    full_name = db.StringField()
    last_name = db.StringField()
    date_of_birth = db.DateTimeField(default=datetime.datetime(1900, 1, 1))
    height = db.IntField(default=0)
    hand = db.StringField(min_length=1, max_length=1, default='U')
    backhand = db.IntField(max_value=2, default=0)
    country = db.StringField(min_length=3, max_length=3, default='XXX')
    image_url = db.StringField()

    meta = {'collection': 'players'}