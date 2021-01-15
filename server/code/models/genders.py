from mongoengine import IntField, StringField
from models.base import BaseModel

class GenderModel(BaseModel):
    '''
    Genders
    '''

    gender_id = IntField(primary_key=True)            
    abbreviation = StringField()
    gender = StringField()

    meta = {'collection': 'genders'}
    
    @classmethod
    def find_by_abbreviation(cls, abbreviation):
        return GenderModel.objects(abbreviation=abbreviation).first()

    @classmethod
    def find_by_gender(cls, gender):
        return GenderModel.objects(gender=gender).first()