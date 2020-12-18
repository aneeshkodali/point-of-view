import requests
from bs4 import BeautifulSoup
from unidecode import unidecode

from models.point import PointModel
from scraper.shot import getShotData


def getPointTable(link_soup):

    '''
    Return point data portion as a table from a match link BeautifulSoup element
    Data is contained in a <table>-like string
    '''

    # point data is in a html-like string called 'pointlog' in 3rd script
    point_data = str(link_soup.select('script')[2])
    point_data = point_data.split('var pointlog = ')[1].split('\n')[0]
    point_table = BeautifulSoup(point_data, 'lxml')

    return point_table

def getPointData(point_table, player_list):
    '''
    Given a HTML table of point data and player array, returns data from that table as an array
    '''

    # initialize array
    points = []
    # initialize point counter
    point_number = 1

    # points data is in 'tr' tags (except for 1st one, which is header)
    points_tr = point_table.select('table tr')[1:]

    # loop through points_tr
    for point_tr in points_tr:
        
        # initialize point dictionary
        point_dict = {}

        # point data are in 'td' tags
        point_td = point_tr.select('td')

        # if empty row, skip
        if [x.text for x in point_td][1:] == ['','','','']:
            continue

        # point_number
        point_dict['point_number'] = point_number

        # server
        try:
            server_name = unidecode(point_td[0].text).strip()
            if server_name:
                server = list(filter(lambda player: player['player_name'] == server_name, player_list))[0]['player_model']
                point_dict['server'] = server
        except:
            pass
            
        # receiver
        try:
            receiver_obj = list(filter(lambda player: player['player_name'] != server_name, player_list))[0]
            receiver_name = receiver_obj['player_name']
            if receiver_name:
                receiver = receiver_obj['player_model']
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
            set_score_server = int(set_score.split('-')[0])
            if set_score_server:
                point_dict['set_score_server'] = set_score_server
        except:
            pass

        # set_score_receiver
        try:
            set_score_receiver = int(set_score_split[1])
            if set_score_receiver:
                point_dict['set_score_receiver'] = set_score_receiver
        except:
            pass

        # set_in_match
        try:
            set_in_match = set_score_server + set_score_receiver
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
            game_score_server = int(game_score.split('-')[0])
            if game_score_server:
                point_dict['game_score_server'] = game_score_server
        except:
            pass

        # game_score_receiver
        try:
            game_score_receiver = int(game_score.split('-')[1])
            if game_score_receiver:
                point_dict['game_score_receiver'] = game_score_receiver
        except:
            pass

        # game_in_set
        try:
            game_in_set = game_score_server + game_score_receiver
            if game_in_set:
                point_dict['game_in_set'] = game_in_set
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
            if point_number == 1:
                point_in_game = 1
            else:            
                point_num_min = [x for x in points if (x['set_score'] == set_score) and (x['game_score'] == game_score)][0]['point_number']
                point_in_game = point_number - point_num_min + 1
            point_dict['point_in_game'] = point_in_game
        except:
            pass

        # side
        try:
            side = getSide(point_score)
            if side:
                point_dict['side'] = side
        except:
            pass

        # num_shots
        try:
            rally = unidecode(point_td[4]).text
            rally_split = rally.split('; ')
            num_shots = len(rally_split)
            if num_shots:
                point_dict['num_shots'] = num_shots
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
                rally_length = num_shots
            elif result in results_lose:
                rally_length = num_shots - 1

            if rally_length:
                point_dict['rally_length'] = rally_length
        except:
            pass

        # winner - number of shots is odd and result is in results_win then server
        try:
            if num_shots % 2 != 0:
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
        try:
            shots = getShotData(rally_split, [server, receiver], result)
            if shots:
                point_dict['shots'] = shots
        except:
            pass
        
        point_model = PointModel(**point_dict)
        points.append(point_model)
        point_number += 1

    return points

def getSide(point_score):

    point_score_deuce = ['0-0', '15-15', '30-0', '0-30', '30-30', '40-15', '15-40', '40-40']
    point_score_ad = ['15-0', '0-15', '30-15', '15-30', '40-0', '0-40', '40-30', '30-40', 'AD-40', '40-AD']

    if point_score in point_score_deuce:
        return 'deuce'
    elif point_score in point_score_ad:
        return 'ad'
    
    point_score_sum = sum([int(x) for x in point_score.split('-')])

    return 'deuce' if point_score_sum % 2 == 0 else 'ad'
