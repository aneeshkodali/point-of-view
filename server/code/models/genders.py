from mongoengine import IntField, StringField

from models.base import BaseModel

class GenderModel(BaseModel):
    '''
    Genders
    '''

    gender_id = IntField(primary_key=True)            
    gender = StringField()

    meta = {'collection': 'genders'}
