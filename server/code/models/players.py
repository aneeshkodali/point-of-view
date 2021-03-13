# python imports
from mongoengine import Document, StringField, DateField, IntField, URLField

# project imoprts
from models.default_values import default_uuid_value, default_date_value
from models.shared.base_mixin import BaseMixin

class PlayerModel(BaseMixin, Document):
    '''
    Players
    '''

    player_id = StringField(primary_key=True, default=default_uuid_value)
    full_name = StringField(default="")
    date_of_birth = DateField(default=default_date_value)
    height = IntField(default=0)
    gender_id = IntField(required=True)
    hand_id = IntField(required=True)
    backhand_id = IntField(required=True)
    country_id = IntField(required=True)
    image_url = URLField(default="")
    link = URLField(unique=True, nullable=False)
    

    meta = {'collection': 'players'}
