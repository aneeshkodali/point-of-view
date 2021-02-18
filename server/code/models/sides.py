from mongoengine import IntField, StringField

from models.base import BaseModel

class SideModel(BaseModel):
    '''
    Sides
    '''

    side_id = IntField(primary_key=True)            
    side = StringField()

    meta = {'collection': 'sides'}
