from mongoengine import IntField, StringField
from models.base import BaseModel

class BackhandModel(BaseModel):
    '''
    Number of hands used for backhand
    In this model, 'backhand_id' is also used for determining number of hands
    '''

    backhand_id = IntField(primary_key=True)
    backhand = StringField()

    meta = {'collection': 'backhands'}

    @classmethod
    def find_by_backhand(cls, backhand):
        return BackhandModel.objects(backhand=backhand).first()