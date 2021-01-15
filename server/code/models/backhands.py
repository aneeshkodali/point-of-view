from mongoengine import IntField, StringField
from models.base import BaseModel

class BackhandModel(BaseModel):
    '''
    Number of hands used for backhand
    '''

    backhand_id = IntField(primary_key=True)
    backhand = StringField()

    meta = {'collection': 'backhands'}

    @classmethod
    def find_by_backhand(cls, backhand):
        return HandModel.objects(backhand=backhand).first()