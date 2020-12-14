from flask_restful import Resource
from models.player import PlayerModel

class Players(Resource):

    # GET method
    def get(self):
        return {'players': [player.json() for player in PlayerModel.objects()]}