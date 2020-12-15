import datetime
import json
from db import db

class PlayerModel(db.Document):

    link = db.URLField()
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

    def json(self):
        return json.loads(self.to_json())

    @classmethod
    def find_by_name(cls, full_name):
        return PlayerModel.objects(full_name=full_name).first()
    
    @classmethod
    def find_by_link(cls, link):
        return PlayerModel.objects(link=link).first()

    @classmethod
    def find_by_id(cls, id):
        return PlayerModel.objects(id=id).first()

