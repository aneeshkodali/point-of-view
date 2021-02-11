#### IMPORTS

## imports from python
from flask import Flask
from flask_mongoengine import MongoEngine
#from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os

## imports from project
#from resources.player import Players, Player, PlayerID
#from resources.match import Matches, MatchesUniqueFieldValues, Match, MatchID
#from resources.tournament import Tournaments, Tournament, TournamentID
from models.match_players import MatchPlayerModel
from models.matches import MatchModel

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
    match = MatchModel.find_by_id(match_id)
    match_json = match.json()

    # convert tournament data to json
    match_json['tournament'] = match_json['tournament'].json()

    # get match players (only need 'player' data and 'win')
    match_players = MatchPlayerModel.objects(match = match)
    match_json['players'] = [{'player': match_player.player.json(), 'win': match_player.win} for match_player in match_players]
    
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
