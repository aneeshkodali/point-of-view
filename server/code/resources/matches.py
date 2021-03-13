# python imports
from flask_restful import Resource

# project imports
from models.matches import MatchModel

class Match(Resource):

    def get(self, match_id):

        # query for match
        match_model = MatchModel.objects(match_id=match_id).first()
        match = match_model.as_dict()

        return {'match': match}

  

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [{k:match[k] for k in ['match_id', 'name']} for match in MatchModel.objects()]}