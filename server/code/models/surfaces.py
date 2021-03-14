# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class SurfaceModel(BaseMixin, Document):
    '''
    Court surfaces
    '''

    surface_id = IntField(primary_key=True)            
    surface = StringField()

    meta = {'collection': 'surfaces'}
    