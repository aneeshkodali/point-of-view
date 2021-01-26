from mongoengine import UUIDField, StringField, DateTimeField, IntField, LazyReferenceField, URLField
import datetime
from uuid import uuid4

from models.base import BaseModel

class PlayerModel(BaseModel):
    '''
    Players
    '''

    player_id = UUIDField(primary_key=True, default=lambda: uuid4(), binary=False)
    full_name = StringField(default="")
    date_of_birth = DateTimeField(default=datetime.datetime(1900, 1, 1))
    height = IntField(default=0)
    gender_id = IntField(default=0)
    hand_id = IntField(default=0)
    backhand_id = IntField(default=0)
    country_id = IntField(default=0)
    image_url = StringField()
    link = URLField(unique=True, nullable=False)
    

    meta = {'collection': 'players'}

    @classmethod
    def find_by_full_name(cls, full_name):
        return PlayerModel.objects(full_name=full_name).first()
    
    @classmethod
    def find_by_link(cls, link):
        return PlayerModel.objects(link=link).first()
