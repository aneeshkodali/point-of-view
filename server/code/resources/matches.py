# python imports
from flask_restful import Resource

# project imports
from models.matches import MatchModel

class Match(Resource):

    def get(self, match_id):

        # query for match
        match_model = MatchModel.objects(match_id=match_id).first()
        match = match_model.as_dict()

        # return match or 404 (not found)
        if match_model:
            return {'match': match}
        return {'message': 'Match not found'}, 404

  

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': match['title'] for match in MatchModel.objects()}