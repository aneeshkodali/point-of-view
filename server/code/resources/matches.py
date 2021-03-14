# python imports
from flask_restful import Resource

# project imports
from models.backhands import BackhandModel
from models.countries import CountryModel
from models.genders import GenderModel
from models.hands import HandModel
from models.levels import LevelModel
from models.match_players import MatchPlayerModel
from models.matches import MatchModel
from models.players import PlayerModel
from models.rounds import RoundModel
from models.surfaces import SurfaceModel
from models.tournament_names import TournamentNameModel
from models.tournaments import TournamentModel

class Match(Resource):

    def get(self, match_id):

        # query for match
        match_model = MatchModel.objects(match_id=match_id).first()
        match = match_model.as_dict()

        # get player data
        match_players = [match_player.as_dict() for match_player in MatchPlayerModel.objects(match_id=match['match_id'])]
        players = []
        for match_player in match_players:
            player = PlayerModel.objects(player_id=match_player['player_id']).first().as_dict()
            player['backhand_id'] = BackhandModel.objects(backhand_id=player['backhand_id']).first().as_dict()
            player['country_id'] = CountryModel.objects(country_id=player['country_id']).first().as_dict()
            player['gender_id'] = GenderModel.objects(gender_id=player['gender_id']).first().as_dict()
            player['hand_id'] = HandModel.objects(hand_id=player['hand_id']).first().as_dict()
            player['win'] = match_player['win']
            players.append(player)
        match['players'] = players

        # get round data
        round_dict = RoundModel.objects(round_id=match['round_id']).first().as_dict()
        match['round_id'] = round_dict

        # get tournament data
        tournament = TournamentModel.objects(tournament_id=match['tournament_id']).first().as_dict()
        tournament['gender_id'] = GenderModel.objects(gender_id=tournament['gender_id']).first().as_dict()
        tournament['level_id'] = LevelModel.objects(level_id=tournament['level_id']).first().as_dict()
        tournament['surface_id'] = SurfaceModel.objects(surface_id=tournament['surface_id']).first().as_dict()
        tournament['tournament_name_id'] = TournamentNameModel.objects(tournament_name_id=tournament['tournament_name_id']).first().as_dict()
        match['tournament'] = tournament


        return {'match': match}

  

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [{k:match[k] for k in ['match_id', 'name']} for match in MatchModel.objects()]}