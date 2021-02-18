from mongoengine import IntField, StringField, ReferenceField

from models.base import BaseModel
from models.default_values import default_uuid_value
from models.player import PlayerModel
from models.sets import SetModel

class GameModel(BaseModel):
    '''
    Games
    '''

    game_id = StringField(primary_key=True, default=default_uuid_value)
    server = ReferenceField(PlayerModel)
    match_set = ReferenceField(SetModel)
    game_in_set = IntField(default=0)
    game_in_match = IntField(default=0)
    score = StringField()

    meta = {'collection': 'games'}

    def json(self):
        return {
            'game_id': self.game_id,
            'server': self.server,
            'match_set': self.match_set,
            'game_in_set': self.game_in_set,
            'game_in_match': self.game_in_match,
            'score': self.score
        }

