from flask_restful import Resource
from models.players import PlayerModel


class Players(Resource):

    # GET method
    def get(self):
        column_list = ['full_name']
        return {'players': [{k:player[k] for k in column_list} for player in PlayerModel.objects()]}