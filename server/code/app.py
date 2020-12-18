#### IMPORTS

## imports from python
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
import os

## imports from project
from db import db
from resources.player import Players, Player
from resources.match import Matches, MatchesUniqueFieldValues, Match, MatchID
from resources.tournament import Tournaments, Tournament, TournamentID

#### APP SETUP

# initialize app
app = Flask(__name__)

# enable cross resource sharing
CORS(app)

# connect db
DB_URI = os.getenv('DB_URI')
app.config['MONGODB_HOST'] = DB_URI
db.init_app(app)

# connect flask_restful api
api = Api(app)


#### ENDPOINT CONFIG
@app.route('/')
def index():
    return 'Hello World'

api.add_resource(Players, '/server/players')
api.add_resource(Player, '/server/player')
api.add_resource(Matches, '/server/matches')
api.add_resource(MatchesUniqueFieldValues, '/server/matches/unique/<field>')
api.add_resource(Match, '/server/match')
api.add_resource(MatchID, '/server/match/<id>')
api.add_resource(Tournaments, '/server/tournaments')
api.add_resource(Tournament, '/server/tournament')
api.add_resource(TournamentID, '/server/tournament/<id>')



#### RUN APP
if __name__ == "__main__":
    app.run(debug=True)
