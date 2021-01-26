from mongoengine import IntField

from models.base import BaseModel

class BackhandModel(BaseModel):
    '''
    Number of hands used for backhand
    '''

    backhand_id = IntField(primary_key=True)
    backhand = IntField()

    meta = {'collection': 'backhands'}

    @classmethod
    def find_by_backhand(cls, backhand):
        return BackhandModel.objects(backhand=backhand).first()