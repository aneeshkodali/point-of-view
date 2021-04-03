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
from models.shots import ShotModel
from models.sides import SideModel
from models.surfaces import SurfaceModel
from models.tournament_names import TournamentNameModel
from models.tournaments import TournamentModel

class Match(Resource):

    def get(self, suffix):

        # query for match
        match_model = MatchModel.objects(suffix=suffix).first()
        match = match_model.as_dict()

        # get player data
        match_players = [match_player.as_dict() for match_player in MatchPlayerModel.objects(match_id=match['match_id']).order_by('-win')]
        players = []
        for match_player in match_players:
            player = PlayerModel.objects(player_id=match_player['player_id']).first().as_dict()

            player['backhand'] = BackhandModel.objects(backhand_id=player['backhand_id']).first().as_dict()['backhand']
            player.pop('backhand_id', None)

            player['country'] = CountryModel.objects(country_id=player['country_id']).first().as_dict()['country']
            player.pop('country_id', None)

            player['gender'] = GenderModel.objects(gender_id=player['gender_id']).first().as_dict()['gender']
            player.pop('gender_id', None)

            player['hand'] = HandModel.objects(hand_id=player['hand_id']).first().as_dict()['hand']
            player.pop('hand_id', None)

            player['score'] = match_player['score']
            player['win'] = match_player['win']
            players.append(player)
        match['players'] = players

        # get round data
        round_name = RoundModel.objects(round_id=match['round_id']).first().as_dict()['round_name']
        match['round'] = round_name
        match.pop('round_id', None)

        # get tournament data
        tournament = TournamentModel.objects(tournament_id=match['tournament_id']).first().as_dict()
        tournament['gender'] = GenderModel.objects(gender_id=tournament['gender_id']).first().as_dict()['gender']
        tournament.pop('gender_id', None)
        tournament['level'] = LevelModel.objects(level_id=tournament['level_id']).first().as_dict()['level']
        tournament.pop('level_id', None)
        tournament['surface'] = SurfaceModel.objects(surface_id=tournament['surface_id']).first().as_dict()['surface']
        tournament.pop('surface_id', None)
        tournament['tournament_name'] = TournamentNameModel.objects(tournament_name_id=tournament['tournament_name_id']).first().as_dict()['tournament_name']
        tournament.pop('tournament_name_id', None)
        match['tournament'] = tournament
        match.pop('tournament_id', None)

        # get set data
        match_sets = [match_set.as_dict() for match_set in SetModel.objects(match_id=match['match_id']).order_by('set_in_match')]
        set_list = []            
        for match_set in match_sets:

            set_dict = {}
            set_dict['set_in_match'] = match_set['set_in_match']
            set_dict['players'] = []

            match_set_players = [set_player.as_dict() for set_player in SetPlayerModel.objects(set_id=match_set['set_id']).order_by('-win')]
            for match_set_player in match_set_players:
                match_set_player_dict = {}
                match_set_player_dict['full_name'] = [player['full_name'] for player in players if player['player_id'] == match_set_player['player_id']][0]
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
                game_dict['players'] = []

                game_players = [game_player.as_dict() for game_player in GamePlayerModel.objects(game_id=game['game_id']).order_by('-win')]
                for game_player in game_players:
                    game_player_dict = {}
                    game_player_dict['full_name'] = [player['full_name'] for player in players if player['player_id'] == game_player['player_id']][0]
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
                    point_dict['side'] = SideModel.objects(side_id=point['side_id']).first().as_dict()['side']
                    point_dict.pop('side_id', None)
                    point_dict['number_of_shots'] = point['number_of_shots']
                    point_dict['rally_length'] = point['rally_length']
                    point_dict['result'] = point['result'] 
                    point_dict['players'] = []

                    point_players = [point_player.as_dict() for point_player in PointPlayerModel.objects(point_id=point['point_id']).order_by('-win')]
                    for point_player in point_players:
                        point_player_dict = {}
                        point_player_dict['full_name'] = [player['full_name'] for player in players if player['player_id'] == point_player['player_id']][0]
                        point_player_dict['score'] = point_player['score']
                        point_player_dict['serve'] = point_player['serve']
                        point_player_dict['win'] = point_player['win']
                        point_dict['players'].append(point_player_dict)

                    # get shot data
                    shots = [shot.as_dict() for shot in ShotModel.objects(point_id=point['point_id']).order_by('shot_number_w_serve')]
                    shot_list = []
                    
                    for shot in shots:
                        shot['shot_by'] = [player['full_name'] for player in players if player['player_id'] == shot['shot_by']][0]
                        shot_list.append(shot)
                    
                    point_dict['shots'] = shot_list

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
        column_list = ['match_id', 'name', 'suffix']
        return {'matches': [{k:match[k] for k in column_list} for match in MatchModel.objects()]}