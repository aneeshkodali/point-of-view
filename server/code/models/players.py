from mongoengine import StringField, DateTimeField, IntField, ReferenceField, URLField
import datetime
from uuid import uuid4

from models.backhands import BackhandModel
from models.base import BaseModel
from models.countries import CountryModel
from models.genders import GenderModel
from models.hands import HandModel

class PlayerModel(BaseModel):
    '''
    Players
    '''

    player_id = StringField(primary_key=True, default=lambda: str(uuid4()))
    full_name = StringField(default="")
    date_of_birth = DateTimeField(default=datetime.datetime(1700, 1, 1))
    height = IntField(default=0)
    gender_id = ReferenceField(GenderModel, default=0)
    hand_id = ReferenceField(HandModel, default=0)
    backhand_id = ReferenceField(BackhandModel, default=0)
    country_id = ReferenceField(CountryModel, default=0)
    image_url = StringField(default="")
    link = URLField(unique=True, nullable=False)
    

    meta = {'collection': 'players'}

    @classmethod
    def find_by_full_name(cls, full_name):
        return PlayerModel.objects(full_name=full_name).first()
    
    @classmethod
    def find_by_link(cls, link):
        return PlayerModel.objects(link=link).first()
