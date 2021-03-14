# python imports
from flask_restful import Resource

# project imports
from models.backhands import BackhandModel
from models.countries import CountryModel
from models.game_players import GamePlayerModel
from models.games import GameModel
from models.genders import GenderModel
from models.hands import HandModel
from models.levels import LevelModel
from models.match_players import MatchPlayerModel
from models.matches import MatchModel
from models.players import PlayerModel
from models.point_players import PointPlayerModel
from models.points import PointModel
from models.rounds import RoundModel
from models.set_players import SetPlayerModel
from models.sets import SetModel
from models.surfaces import SurfaceModel
from models.tournament_names import TournamentNameModel
from models.tournaments import TournamentModel

class Match(Resource):

    def get(self, match_id):

        # query for match
        match_model = MatchModel.objects(match_id=match_id).first()
        match = match_model.as_dict()

        # get player data
        match_players = [match_player.as_dict() for match_player in MatchPlayerModel.objects(match_id=match['match_id']).order_by('-win')]
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

        # get set data
        match_sets = [match_set.as_dict() for match_set in SetModel.objects(match_id=match['match_id']).order_by('set_in_match')]
        set_list = []            
        for match_set in match_sets:

            set_dict = {}
            set_dict['set_in_match'] = match_set['set_in_match']
            set_dict['score'] = match_set['score']
            set_dict['players'] = []

            match_set_players = [set_player.as_dict() for set_player in SetPlayerModel.objects(set_id=match_set['set_id']).order_by('-win')]
            for match_set_player in match_set_players:
                match_set_player_dict = {}
                match_set_player_dict['player'] = [player['full_name'] for player in players if player['player_id'] == match_set_player['player_id']][0]
                match_set_player_dict['score'] = match_set_player['score']
                match_set_player_dict['win'] = match_set_player['win']
                set_dict['players'].append(match_set_player_dict)

            # get game data
            games = [game.as_dict() for game in GameModel.objects(set_id=match_set['set_id']).order_by('game_in_match')]
            game_list = []
            for game in games:

                game_dict = {}
                game_dict['game_in_set'] = game['game_in_set']
                game_dict['game_in_match'] = game['game_in_match']
                game_dict['score'] = game['score']
                game_dict['players'] = []

                game_players = [game_player.as_dict() for game_player in GamePlayerModel.objects(game_id=game['game_id']).order_by('-win')]
                for game_player in game_players:
                    game_player_dict = {}
                    game_player_dict['player'] = [player['full_name'] for player in players if player['player_id'] == game_player['player_id']][0]
                    game_player_dict['score'] = game_player['score']
                    game_player_dict['win'] = game_player['win']
                    game_dict['players'].append(game_player_dict)
                
                # get point data
                points = [point.as_dict() for point in PointModel.objects(game_id=game['game_id']).order_by('point_in_match')]
                point_list = []
                for point in points:

                    point_dict = {}
                    point_dict['point_in_game'] = point['point_in_game']
                    point_dict['point_in_set'] = point['point_in_set']
                    point_dict['point_in_match'] = point['point_in_match']
                    point_dict['score'] = point['score']
                    point_dict['players'] = []

                    point_players = [point_player.as_dict() for point_player in PointPlayerModel.objects(point_id=point['point_id']).order_by('-win')]
                    for point_player in point_players:
                        point_player_dict = {}
                        point_player_dict['player'] = [player['full_name'] for player in players if player['player_id'] == point_player['player_id']][0]
                        point_player_dict['score'] = point_player['score']
                        point_player_dict['serve'] = point_player['serve']
                        point_player_dict['win'] = point_player['win']
                        point_dict['players'].append(point_player_dict)

                    point_list.append(point_dict)

                game_dict['points'] = point_list

                game_list.append(game_dict)
            
            set_dict['games'] = game_list

            set_list.append(set_dict)
        match['sets'] = set_list


        return {'match': match}

  

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [{k:match[k] for k in ['match_id', 'name']} for match in MatchModel.objects()]}