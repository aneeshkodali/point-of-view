from mongoengine import StringField, DateTimeField, IntField, ReferenceField, URLField

from models.backhands import BackhandModel
from models.base import BaseModel
from models.countries import CountryModel
from models.default_values import default_uuid_value, default_date_value
from models.genders import GenderModel
from models.hands import HandModel

class PlayerModel(BaseModel):
    '''
    Players
    '''

    player_id = StringField(primary_key=True, default=default_uuid_value)
    full_name = StringField(default="")
    date_of_birth = DateTimeField(default=default_date_value)
    height = IntField(default=0)
    gender = ReferenceField(GenderModel)
    hand = ReferenceField(HandModel)
    backhand = ReferenceField(BackhandModel)
    country = ReferenceField(CountryModel)
    image_url = URLField(default="")
    link = URLField(unique=True, nullable=False)
    

    meta = {'collection': 'players'}

    def json(self):
        return {
            'player_id': self.player_id,
            'full_name': self.full_name,
            'date_of_birth': self.date_of_birth,
            'height': self.height,
            'gender': self.gender,
            'hand': self.hand,
            'backhand': self.backhand,
            'country': self.country,
            'image_url': self.image_url,
            'link': self.link
        }
