from flask_restful import Resource, reqparse
import json
from models.match import MatchModel
from scraper.match import getMatchData

class Match(Resource):

    # create parser
    parser = reqparse.RequestParser()
    parser.add_argument('link',
                        type=str,
                        required=True,
                        help='Must supply link'
                        )

    # POST method
    def post(self):

        # get link from request
        data = Match.parser.parse_args()
        link = data['link']

        # insert match data
        match_data = getMatchData(link)
        match_model = MatchModel(**match_data)
        # insert into db, return 'server' error
        try:
            match_model.save()
        except Exception as e:
            return {
                    'message': 'An error occurred inserting the match',
                    'error': str(e)
                    }, 500
        
        return match_model.json(), 201


class MatchID(Resource):

    # GET method
    def get(self, id):
        match = MatchModel.find_by_id(id)
        if match:
            return match.json()
        return {'message': 'Item not found'}, 404

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': json.loads(MatchModel.objects().fields(title=1).to_json())}