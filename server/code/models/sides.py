# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class SideModel(BaseMixin, Document):
    '''
    Sides
    '''

    side_id = IntField(primary_key=True)            
    side = StringField()

    meta = {'collection': 'sides'}
