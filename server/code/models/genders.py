# python imports
from mongoengine import Document, IntField, StringField

# project imports
from models.shared.base_mixin import BaseMixin

class GenderModel(BaseMixin, Document):
    '''
    Genders
    '''

    gender_id = IntField(primary_key=True)            
    gender = StringField()

    meta = {'collection': 'genders'}
