from mongoengine import IntField, StringField
from models.base import BaseModel

class CountryModel(BaseModel):
    '''
    Countries
    '''

    country_id = IntField(primary_key=True)
    country = StringField(unique=True, nullable=False)
    code_three = StringField(unique=True, nullable=False)

    meta = {'collection': 'countries'}

    @classmethod
    def find_by_country(cls, country):
        return CountryModel.objects(country=country).first()

    @classmethod
    def find_by_code_three(cls, code_three):
        return CountryModel.objects(code_three=code_three).first()