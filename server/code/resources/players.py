from flask_restful import Resource, request
from models.players import PlayerModel


class Players(Resource):

    # GET method
    def get(self):

        players = PlayerModel.objects.filter(**request.args)
        column_list = ['full_name', 'link']
        return {'players': [{k:player[k] for k in column_list} for player in players]}