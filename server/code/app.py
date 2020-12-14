#### IMPORTS

## imports from python
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
load_dotenv()
import os

## imports from project
from db import db
from resources.player import Players
from resources.match import Matches, Match

#### APP SETUP

# initialize app
app = Flask(__name__)

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
api.add_resource(Matches, '/server/matches')
api.add_resource(Match, '/server/match')


#### RUN APP
if __name__ == "__main__":
    app.run(debug=True)
