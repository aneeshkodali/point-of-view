from mongoengine import IntField

from models.base import BaseModel

class BackhandModel(BaseModel):
    '''
    Number of hands used for backhand
    '''

    backhand_id = IntField(primary_key=True)
    backhand = IntField()

    meta = {'collection': 'backhands'}
