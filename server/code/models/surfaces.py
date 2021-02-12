from mongoengine import IntField, StringField

from models.base import BaseModel

class SurfaceModel(BaseModel):
    '''
    Court surfaces
    '''

    surface_id = IntField(primary_key=True)            
    surface = StringField()

    meta = {'collection': 'surfaces'}
    