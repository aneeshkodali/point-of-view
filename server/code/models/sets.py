from mongoengine import IntField, StringField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value, default_date_value
from models.matches import MatchModel

class SetModel(BaseModel):
    '''
    Sets
    '''

    set_id = StringField(primary_key=True, default=default_uuid_value)
    match = ReferenceField(MatchModel)
    set_in_match = IntField(default=0)
    score = StringField(default="0-0")

    meta = {'collection': 'sets'}

    def json(self):
        return {
            'set_id': self.set_id,
            'match_id': self.match,
            'set_in_match': self.set_in_match,
            'score': self.score
        }

