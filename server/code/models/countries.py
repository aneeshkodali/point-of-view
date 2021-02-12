from mongoengine import IntField, StringField

from models.base import BaseModel

class CountryModel(BaseModel):
    '''
    Countries
    '''

    country_id = IntField(primary_key=True)
    country = StringField()

    meta = {'collection': 'countries'}
