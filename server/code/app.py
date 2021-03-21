#### IMPORTS

## python imports
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_restful import Api
from mongoengine.queryset.visitor import Q

## project imports
from resources.matches import Match, Matches


#### APP SETUP

# initialize app
app = Flask(__name__)

# configure app
app.config.from_object('config.DevConfig')

# enable cross resource sharing
CORS(app)

# connect db
db = MongoEngine(app)

# connect flask_restful api
api = Api(app)


#### ROUTE CONFIG
@app.route('/')
def index():
    return 'Hello World'

api.add_resource(Match, '/server/matches/<string:suffix>')
api.add_resource(Matches, '/server/matches')

#### RUN APP
if __name__ == "__main__":
    app.run()
