# python imports
from bs4 import BeautifulSoup
from unidecode import unidecode
import pandas as pd
import requests

# project imports
from models.games import GameModel
from models.game_players import GamePlayerModel
from models.point_players import PointPlayerModel
from models.points import PointModel
from models.sides import SideModel
from models.sets import SetModel
from models.set_players import SetPlayerModel
from models.sides import SideModel
from scraper.shots import getShotData

def getPointData(match_soup, match_id, player_id_dict):
    '''
    Creates/inserts the appropriate data
    '''
    # create list of playe names
    player_list = [k for k in player_id_dict]

    # get dataframe
    point_df = makePointDF(match_soup, player_list)

    # get list of set numbers
    sets_in_match = list(point_df['set_in_match'].unique())
    sets_in_match.sort()

    # loop through sets_in_match
    for set_in_match in sets_in_match:

        # filter for set
        set_df = point_df.loc[point_df['set_in_match'] == set_in_match]
        # get set score by getting last game_score in the set and incrementing winner score
        last_point_in_set = set_df.iloc[-1]
        server = last_point_in_set['server']
        winner = last_point_in_set['winner']
        loser = last_point_in_set['loser']
        game_score_server = int(last_point_in_set['game_score_server'])
        game_score_receiver = int(last_point_in_set['game_score_receiver'])
        game_score_winner = game_score_server+1 if winner == server else game_score_receiver+1
        game_score_loser = game_score_server if winner != server else game_score_receiver
        set_score = f"{game_score_winner}-{game_score_loser}"

        # create SetModel
        set_model = SetModel(**{'set_in_match': set_in_match, 'match_id': match_id, 'score': set_score})
        set_model.save()
        set_id = set_model['set_id']

        # create SetPlayerModel
        SetPlayerModel(**{'set_id': set_id, 'player_id': player_id_dict[winner], 'win': 1, 'score': game_score_winner}).save()
        SetPlayerModel(**{'set_id': set_id, 'player_id': player_id_dict[loser], 'win': 0, 'score': game_score_loser}).save()  

        # get list of games
        games_in_set = list(set_df['game_in_set'].unique())
        games_in_set.sort()

        # loop through games_in_set
        for game_in_set in games_in_set:

            # filter for game
            game_df = set_df.loc[set_df['game_in_set'] == game_in_set]
            # get game score by getting last game_score in the set and incrementing winner score
            first_point_in_game = game_df.iloc[0]
            server = first_point_in_game['server']
            last_point_in_game = game_df.iloc[-1]
            game_in_set = last_point_in_game['game_in_set']
            game_in_match = last_point_in_game['game_in_match']
            winner = last_point_in_game['winner']
            loser = last_point_in_game['loser']
            game_score = last_point_in_game['game_score']
            game_score_server = last_point_in_game['game_score_server']
            game_score_receiver = last_point_in_game['game_score_receiver']
            game_score_winner = game_score_server if winner == server else game_score_receiver
            game_score_loser = game_score_server if winner != server else game_score_receiver
            serve = (server == winner)*1

            # create GameModel
            game_model = GameModel(**{'match_set': set_model, 'game_in_set': game_in_set, 'game_in_match': game_in_match, 'score': game_score})
            game_model.save()

            # Create GamePlayerModel
            GamePlayerModel(**{'game': game_model, 'player': player_model_dict[winner], 'win': 1, 'serve': serve, 'score': game_score_winner}).save()
            GamePlayerModel(**{'game': game_model, 'player': player_model_dict[loser], 'win': 0, 'serve': serve, 'score': game_score_loser}).save()

            # get list of points
            points_in_game = list(game_df['point_in_game'].unique())
            points_in_game.sort()

            # loop through points_in_game
            for point_in_game in points_in_game:

                # filter for point (should only be one row)
                point = game_df.loc[game_df['point_in_game'] == point_in_game].iloc[0]
                server = point['server']
                receiver = point['receiver']
                point_in_set = point['point_in_set']
                point_in_match = point['point_in_match']
                winner = point['winner']
                loser = point['loser']
                point_score = point['point_score']
                point_score_server = point['point_score_server']
                point_score_receiver = point['point_score_receiver']
                point_score_winner = point_score_server if winner == server else point_score_receiver
                point_score_loser = point_score_server if winner != server else point_score_receiver
                serve = (server == winner)*1
                number_of_shots = point['number_of_shots']
                rally_length = point['rally_length']
                rally_split = point['rally_split']
                result = point['result']

                if result == 'double fault':
                    rally_length = 0

                side = getSide(point_score)
                side_model = getSideModel(side)

                # create PointModel
                point_model = PointModel(**{'game': game_model, 'point_in_game': point_in_game, 'point_in_set': point_in_set, 'point_in_match': point_in_match, 'number_of_shots': number_of_shots, 'rally_length': rally_length, 'result': result, 'side': side_model, 'score': point_score})
                point_model.save()

                # create PointPlayerModel
                PointPlayerModel(**{'point': point_model, 'player': player_model_dict[winner], 'win': 1, 'serve': serve, 'score': point_score_winner}).save()
                PointPlayerModel(**{'point': point_model, 'player': player_model_dict[loser], 'win': 0, 'serve': serve, 'score': point_score_loser}).save()

                # get shot data
                player_model_list = [player_model_dict[server], player_model_dict[receiver]]
                getShotData(rally_split, player_model_list, result)



    return

def makePointDF(match_soup, player_list):
    '''
    Given
        - match_soup: BeautifulSoup soup element for match
        - player_list: list of player_names
    Return dataframe of points
    '''

    # get point_table
    point_table = getPointTable(match_soup)

    # initialize array
    points = []
    # initialize point counter
    point_in_match = 1

    # loop through point_table (each row is a <tr>)
    for point_tr in point_table:
        
        # initialize point dictionary
        point_dict = {}

        # point data are in 'td' tags
        point_td = point_tr.select('td')

        # if empty row, skip
        if [x.text for x in point_td][1:] == ['','','','']:
            continue

        # point_in_match
        point_dict['point_in_match'] = point_in_match

        # server
        try:
            server = unidecode(point_td[0].text).strip()
            if server:
                point_dict['server'] = server
        except:
            pass
            
        # receiver
        try:
            receiver = list(filter(lambda player: player != server, player_list))[0]
            if receiver:
                point_dict['receiver'] = receiver
        except:
            pass


        # set_score
        try:
            set_score = unidecode(point_td[1].text)
            if set_score:
                point_dict['set_score'] = set_score
                
        except:
            pass

        # set_score_server
        try:
            set_score_server = set_score.split('-')[0]
            if set_score_server:
                point_dict['set_score_server'] = set_score_server
        except:
            pass

        # set_score_receiver
        try:
            set_score_receiver = set_score.split('-')[1]
            if set_score_receiver:
                point_dict['set_score_receiver'] = set_score_receiver
        except:
            pass

        # set_in_match
        try:
            set_in_match = int(set_score_server) + int(set_score_receiver) + 1
            if set_in_match:
                point_dict['set_in_match'] = set_in_match
        except:
            pass

        # game_score
        try:
            game_score = unidecode(point_td[2].text)
            if game_score:
                point_dict['game_score'] = game_score
        except:
            pass

        # game_score_server
        try:
            game_score_server = game_score.split('-')[0]
            if game_score_server:
                point_dict['game_score_server'] = game_score_server
        except:
            pass

        # game_score_receiver
        try:
            game_score_receiver = game_score.split('-')[1]
            if game_score_receiver:
                point_dict['game_score_receiver'] = game_score_receiver
        except:
            pass

        # game_in_set
        try:
            game_in_set = int(game_score_server) + int(game_score_receiver) + 1
            if game_in_set:
                point_dict['game_in_set'] = game_in_set
        except:
            pass

        # game_in_match
        try:
            if set_in_match == 1:
                game_in_match = game_in_set
            else:
                game_in_last_set = max([x['game_in_set'] for x in points if x['set_in_match'] == (set_in_match-1)])
                game_in_match = game_in_last_set + game_in_set
            point_dict['game_in_match'] = game_in_match
        except:
            pass

        # point_score
        try:
            point_score = unidecode(point_td[3].text)
            if point_score:
                point_dict['point_score'] = point_score
        except:
            pass

        # point_score_server
        try:
            point_score_server = point_score.split('-')[0]
            if point_score_server:
                point_dict['point_score_server'] = point_score_server
        except:
            pass

        # point_score_receiver
        try:
            point_score_receiver = point_score.split('-')[1]
            if point_score_receiver:
                point_dict['point_score_receiver'] = point_score_receiver
        except:
            pass      

        # point_in_game
        try:
            point_num_min = min([x['point_in_match'] for x in points if (x['set_score'] == set_score) and (x['game_score'] == game_score)] or [point_in_match])
            point_in_game = point_in_match - point_num_min + 1
            point_dict['point_in_game'] = point_in_game
        except:
            pass

        # point_in_set
        try:
          
            point_num_min = min([x['point_in_match'] for x in points if x['set_score'] == set_score] or [point_in_match])
            point_in_set = point_in_match - point_num_min + 1
            point_dict['point_in_set'] = point_in_set
        except:
            pass

        # side
        try:
            side = getSide(point_score)
            if side:
                point_dict['side'] = side
        except:
            pass

        # rally list
        try:
            rally = unidecode(point_td[4]).text
            rally_split = rally.split('; ')
            if rally_split:
                point_dict['rally_split'] = rally_split
        except:
            pass

        # number_of_shots
        try:
            number_of_shots = len(rally_split)
            if number_of_shots:
                point_dict['number_of_shots'] = number_of_shots
        except:
            pass

        # result
        try:
            result = unidecode(point_td[4].select('b')[0].text.strip())
            if result:
                point_dict['result'] = result
        except:
            pass

        results_win = ['ace', 'service winner', 'winner']
        results_lose = ['double fault', 'forced error', 'unforced error']

        # rally_length
        try:
            if result in results_win:
                rally_length = number_of_shots
            elif result in results_lose:
                rally_length = number_of_shots - 1

            if rally_length:
                point_dict['rally_length'] = rally_length
        except:
            pass

        # winner - number of shots is odd and result is in results_win then server
        try:
            if number_of_shots % 2 != 0:
                if result in results_win:
                    winner = server
                elif result in results_lose:
                    winner = receiver
            else:
                if result in results_win:
                    winner = receiver
                elif result in results_lose:
                    winner = server

            if winner:
                point_dict['winner'] = winner
        except:
            pass

        # loser
        try:
            loser = server if winner == receiver else receiver
            if loser:
                point_dict['loser'] = loser
        except:
            pass

        # shots
        #try:
        #    shots = getShotData(rally_split, [server, receiver], result)
        #    if shots:
        #        point_dict['shots'] = shots
        #except:
        #    pass
        
        points.append(point_dict)
        point_in_match += 1
    
    points_df = pd.DataFrame(points)
    return points_df


def getPointTable(link_soup):

    '''
    Return point data portion as a table from a match link BeautifulSoup element
    Data is contained in a <table>-like string
    '''

    # point data is in a html-like string called 'pointlog' in 3rd script
    point_data = str(link_soup.select('script')[2])
    point_data = point_data.split('var pointlog = ')[1].split('\n')[0]
    point_table = BeautifulSoup(point_data, 'lxml')
    # points data is in 'tr' tags (except for 1st one, which is header)
    point_table = point_table.select('table tr')[1:]

    return point_table


def getSide(point_score):

    point_score_deuce = ['0-0', '15-15', '30-0', '0-30', '30-30', '40-15', '15-40', '40-40']
    point_score_ad = ['15-0', '0-15', '30-15', '15-30', '40-0', '0-40', '40-30', '30-40', 'AD-40', '40-AD']

    if point_score in point_score_deuce:
        return 'deuce'
    elif point_score in point_score_ad:
        return 'ad'
    
    point_score_sum = sum([int(x) for x in point_score.split('-')])

    return 'deuce' if point_score_sum % 2 == 0 else 'ad'

def getSideModel(side):
    '''
    Takes a round and queries RoundModel for record
    Return record or create new one if not found
    '''
    side_model_db = SideModel.objects(side=side).first()
    if side_model_db:
        return side_model_db

    side_id_new = max([side_model['side_id'] for side_model in SideModel.objects()] or [0]) + 1
    side_model_new = SideModel(**{'side_id': side_id_new, 'side': side})
    side_model_new.save()

    return side_model_new