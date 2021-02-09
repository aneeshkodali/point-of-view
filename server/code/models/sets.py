from mongoengine import IntField, StringField, ReferenceField
from mongoengine.queryset.visitor import Q

from models.base import BaseModel
from models.default_values import default_uuid_value, default_date_value
from models.matches import MatchModel

class SetModel(BaseModel):
    '''
    Sets
    '''

    set_id = StringField(primary_key=True, default=default_uuid_value)
    match_id = ReferenceField(MatchModel)
    set_in_match = IntField(default=0)
    score = StringField(default="")

    meta = {'collection': 'sets'}

    def json(self):
        return {
            'set_id': self.set_id,
            'match_id': self.match_id,
            'set_in_match': self.set_in_match,
            'score': self.score
        }

    @classmethod
    def find_by_set_in_match_and_match_id(cls, set_in_match, match_id):
        return SetModel.objects(Q(set_in_match=set_in_match) & Q(match_id=match_id)).first()

    @classmethod
    def find_by_set_id_and_match_id(cls, set_id, match_id):
        return SetModel.objects(Q(set_id=set_id) & Q(match_id=match_id)).first()
