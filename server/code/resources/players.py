from flask_restful import Resource, request
from models.players import PlayerModel

class Player(Resource):

    # GET method
    def get(self, player_name):

        # query for player
        player_full_name = player_name.replace('_',' ')
        player = PlayerModel.objects(full_name=player_full_name).first().as_dict()
        return {'player': player}


class Players(Resource):

    # GET method
    def get(self):

        players = PlayerModel.objects.filter(**request.args)
        column_list = ['full_name', 'link']
        return {'players': [{k:player[k] for k in column_list} for player in players]}