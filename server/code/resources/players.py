from flask_restful import Resource, request

from models.backhands import BackhandModel
from models.countries import CountryModel
from models.genders import GenderModel
from models.hands import HandModel
from models.match_players import MatchPlayerModel
from models.matches import MatchModel
from models.players import PlayerModel

class Player(Resource):

    # GET method
    def get(self, player_name):

        # query for player
        player_full_name = player_name.replace('_',' ')
        player = PlayerModel.objects(full_name=player_full_name).first().as_dict()

        # replace backhand key-value pair
        player['backhand'] = BackhandModel.objects(backhand_id=player['backhand_id']).first().as_dict()['backhand']
        player.pop('backhand_id', None)

        # replace country key-value pair
        player['country'] = CountryModel.objects(country_id=player['country_id']).first().as_dict()['country']
        player.pop('country_id', None)

        # replace gender key-value pair
        player['gender'] = GenderModel.objects(gender_id=player['gender_id']).first().as_dict()['gender']
        player.pop('gender_id', None)

        # replace hand key-value pair
        player['hand'] = HandModel.objects(hand_id=player['hand_id']).first().as_dict()['hand']
        player.pop('hand_id', None)

        # get player matches
        player_match_players = MatchPlayerModel.objects(player_id=player['player_id'])
        player_match_ids = [match_player['match_id'] for match_player in player_match_players]
        match_column_list = ['match_id', 'name', 'suffix']
        player_matches = [{k:match[k] for k in match_column_list} for match in MatchModel.objects(match_id__in=player_match_ids)]
        player['matches'] = player_matches

        return {'player': player}


class Players(Resource):

    # GET method
    def get(self):

        players = PlayerModel.objects.filter(**request.args)
        column_list = ['full_name', 'link']
        return {'players': [{k:player[k] for k in column_list} for player in players]}