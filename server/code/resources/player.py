from flask_restful import Resource, reqparse
from models.players import PlayerModel
from scraper.player import constructPlayerLink, getPlayerData

class Player(Resource):

    # POST method
    def post(self):
        # create parser
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='Must provide player name'
                            )
        parser.add_argument('gender',
                            type=str,
                            required=True,
                            help='Must provide player gender'
                            )

        # get data from parser
        data = parser.parse_args()
        name = data['name']

        # if player exists, return 'bad request' error
        if PlayerModel.find_by_full_name(name):
            return {'message': f"Player '{name}' already exists"}, 400

    
        # create Player object
        player_link = constructPlayerLink(**data)
        player_data = getPlayerData(player_link)
        player_model = PlayerModel(**player_data)

        # insert into db, return 'server' error
        try:
            player_model.save()
        except Exception as e:
            return {
                    'message': 'An error occurred inserting the player',
                    'error': str(e)
                    }, 500
        
        return player_model.json(), 201

class PlayerID(Resource):

    # GET method
    def get(self, id):
        player = PlayerModel.find_by_id(id)
        if player:
            return player.json()
        return {'message': 'Player not found'}, 404

class Players(Resource):

    # GET method
    def get(self):
        return {'players': json.loads(PlayerModel.objects().fields(title=1).to_json())}