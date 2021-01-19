from mongoengine import IntField, StringField

from models.base import BaseModel

class SurfaceModel(BaseModel):
    '''
    Court surfaces
    '''

    surface_id = IntField(primary_key=True)            
    surface = StringField()

    meta = {'collection': 'surfaces'}
    
    @classmethod
    def find_by_surface(cls, surface):
        return SurfaceModel.objects(surface=surface).first()