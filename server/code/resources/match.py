from flask_restful import Resource, reqparse
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

        # get match_data
        match_data = getMatchData(link)

        return {'match': match_data}

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [match.json() for match in MatchModel.objects()]}