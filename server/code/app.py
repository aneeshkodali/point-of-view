#### IMPORTS

## imports from python
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from mongoengine.queryset.visitor import Q
load_dotenv()
import os

## imports from project
#from resources.player import Players, Player, PlayerID
#from resources.match import Matches, MatchesUniqueFieldValues, Match, MatchID
#from resources.tournament import Tournaments, Tournament, TournamentID
from models.match_players import MatchPlayerModel
from models.matches import MatchModel
from models.set_players import SetPlayerModel
from models.sets import SetModel

#### APP SETUP

# initialize app
app = Flask(__name__)

# enable cross resource sharing
CORS(app)

# connect db
DB_URI = os.getenv('DB_URI')
app.config['MONGODB_HOST'] = DB_URI
db = MongoEngine(app)

# connect flask_restful api
#api = Api(app)


#### ENDPOINT CONFIG
@app.route('/')
def index():
    return 'Hello World'

@app.route('/server/matches')
def get_matches():
    return {'matches': MatchModel.objects().fields(match_id=1, link=1)}

@app.route('/server/matches/<string:match_id>')
def get_match_data(match_id):

    # get match
    match = MatchModel.objects(match_id=match_id).first()
    match_json = match.json()

    # format players
    match_players = MatchPlayerModel.objects(match=match)
    match_json['players'] = []
    for match_player in match_players:
        match_player_dict = {}
        match_player_dict['player'] = match_player.player.json()
        match_player_dict['player']['backhand'] = match_player_dict['player']['backhand']['backhand']
        match_player_dict['player']['country'] = match_player_dict['player']['country']['country']
        match_player_dict['player']['gender'] = match_player_dict['player']['gender']['gender']
        match_player_dict['player']['hand'] = match_player_dict['player']['hand']['hand']
        match_player_dict['win'] = match_player.win
        match_json['players'].append(match_player_dict)

    # format round
    match_json['match_round'] = match_json['match_round']['round_name']

    # format tournament
    match_json['tournament'] = match_json['tournament'].json()
    match_json['tournament']['gender'] =  match_json['tournament']['gender']['gender']
    match_json['tournament']['level'] =  match_json['tournament']['level']['level']
    match_json['tournament']['surface'] =  match_json['tournament']['surface']['surface']
    match_json['tournament']['tournament_name'] =  match_json['tournament']['tournament_name']['tournament_name']

    # format sets
    match_sets = SetModel.objects(match=match)
    match_json['sets'] = []
    for match_set in match_sets:
        set_player = SetPlayerModel.objects(Q(match_set=match_set) & Q(win=1)).first().player.full_name
        match_set_dict = {}
        match_set_dict['set_in_match'] = match_set['set_in_match']
        match_set_dict['winner'] = set_player
        match_set_dict['score'] = match_set['score']
        match_json['sets'].append(match_set_dict)

    return {'data': match_json}

#api.add_resource(Players, '/server/players')
#api.add_resource(Player, '/server/player')
#api.add_resource(PlayerID, '/server/player/<id>')
#api.add_resource(Matches, '/server/matches')
#api.add_resource(MatchesUniqueFieldValues, '/server/matches/unique/<field>')
#api.add_resource(Match, '/server/match')
#api.add_resource(MatchID, '/server/match/<id>')
#api.add_resource(Tournaments, '/server/tournaments')
#api.add_resource(Tournament, '/server/tournament')
#api.add_resource(TournamentID, '/server/tournament/<id>')



#### RUN APP
if __name__ == "__main__":
    app.run(debug=True)
