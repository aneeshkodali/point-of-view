from flask_restful import Resource
from models.tournament import TournamentModel

class Tournaments(Resource):

    # GET method
    def get(self):
        return {'tournaments': [tournament.json() for tournament in TournamentModel.objects()]}