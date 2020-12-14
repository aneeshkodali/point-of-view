from flask_restful import Resource
from models.match import MatchModel

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [match.json() for match in MatchModel.objects()]}