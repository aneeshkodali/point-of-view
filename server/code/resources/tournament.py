from flask_restful import Resource, reqparse
from models.tournament import TournamentModel
from scraper.tournament import constructTournamentLink, getTournamentData

class Tournament(Resource):

    
    # GET - get info about one tournament
    def get(self):

        # create parser
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='Must provide tournament name'
                            )
        parser.add_argument('gender',
                            type=str,
                            required=True,
                            help='Must provide tournament gender'
                            )

        # get data from request body
        data = parser.parse_args()
        name = data['name']
        gender = data['gender']

        tournament = TournamentModel.find_by_name_and_gender(name, gender)
        # if tournament exists, return it, else return 'not found' error
        if tournament:
            return tournament.json()
        return {'message': f"Tournament '{name}' for gender '{gender}' not found"}, 404

    # POST - create new tournament
    def post(self):
        
        # create parser
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='Must provide tournament name'
                            )
        parser.add_argument('gender',
                            type=str,
                            required=True,
                            help='Must provide tournament gender'
                            )
        parser.add_argument('year',
                    type=str,
                    required=True,
                    help='Must provide a year'
                    )

        # get data from request body
        data = Tournament.parser.parse_args()
        name = data['name']
        gender = data['gender']
        
        # if tournament exists, return 'bad request' error
        if TournamentModel.find_by_name_and_gender(name, gender):
            return {'message': f"Tournament '{name}' for gender '{gender}' already exists"}, 400

    
        # create Tournament object
        tournament_link = constructTournamentLink(**data)
        tournament_data = getTournamentData(tournament_link)
        tournament_model = TournamentModel(**tournament_data)

        # insert into db, return 'server' error
        try:
            tournament_model.save()
        except:
            return {'message': 'An error occurred inserting the tournament'}, 500
        
        return tournament_model.json(), 201


class Tournaments(Resource):

    # GET method
    def get(self):
        return {'tournaments': [tournament.json() for tournament in TournamentModel.objects()]}