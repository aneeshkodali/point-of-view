# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class CountryModel(BaseMixin, Document):
    '''
    Countries
    '''

    country_id = IntField(primary_key=True)
    country = StringField()

    meta = {'collection': 'countries'}
