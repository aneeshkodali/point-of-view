from flask_restful import Resource, reqparse
from models.match import MatchModel
from scraper.match import getMatchData
from scraper.tournament import constructTournamentLink, getTournamentData

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

        # get tournament data
        tournament_name = match_data['tournament']
        tournament_year = match_data['match_date'][:4]
        tournament_gender = match_data['gender']
        tournament_link = constructTournamentLink(year=tournament_year, name=tournament_name, gender=tournament_gender)
        tournament_data = getTournamentData(tournament_link)

        return {'tournament': tournament_data, 'match': match_data}

class Matches(Resource):

    # GET method
    def get(self):
        return {'matches': [match.json() for match in MatchModel.objects()]}