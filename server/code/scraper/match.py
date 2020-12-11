import requests
from bs4 import BeautifulSoup
import datetime
from unidecode import unidecode



def getMatchData(link):

    '''
    Takes in a match link and returns a dictionary of match data
    '''

    # initialize match dictionary
    match_dict = {}
    match_dict['link'] = link

    # parse link for data
    # after the stem, link is of the form <date>-<gender>-<tournament>-<round>-<player1>-<player2>.html
    suffix = link.split('http://www.tennisabstract.com/charting/')[1].split('-')

    # date
    try:
        match_date = suffix[0]
        if match_date:
            year = int(match_date[:4])
            month = int(match_date[4:6])
            day = int(match_date[6:])
            match_dict['match_date'] = datetime.datetime(year, month, day)
    except:
        pass
    
    # gender
    try:
        gender = suffix[1]
        if gender:
            match_dict['gender'] = gender
    except:
        pass

    # tournament
    try:
        tournament = suffix[2].replace('_', ' ')
        if tournament:
            match_dict['tournament'] = tournament
    except:
        pass

    # round
    try:
        match_round = suffix[3]
        if match_round:
            match_dict['match_round'] = match_round
    except:
        pass

    # player1 and player2
    try:
        player_one = suffix[4].replace('_', ' ')
        player_two = suffix[5].replace('_', ' ').replace('.html','')
        players = [player_one, player_two]
        if players:
            match_dict['players'] = players
    except:
        pass

    # get BeautifulSoup object
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'lxml')
    except:
        pass

    # title
    try:
        title = soup.select('h2')[0].text
        if title:
            match_dict['title'] = title
    except:
        pass

    # result
    try:
        result = soup.select('b')[0].text
        if result:
            match_dict['result'] = result
    except:
        pass

    # winner
    try:
        winner = result.split(' d.')[0]
        if winner:
            match_dict['winner'] = winner
    except:
        pass

    # loser
    try:
        loser = list(filter(lambda player: player != winner, players))[0]
        if loser:
            match_dict['loser'] = loser
    except:
        pass

    # score
    try:
        score = result.split(f"{loser} ")[1]
        if score:
            match_dict['score'] = score
    except:
        pass

    # sets
    try:
        sets = score.split(' ')
        if sets:
            match_dict['sets'] = len(sets)
    except:
        pass

   
    # points
    try:
        point_table = getPointTable(soup)
        if point_table:
            points_data = getPointData(point_table, players)
            match_dict['points'] = points_data
    except:
        pass

    return match_dict['points']

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
    for point_tr in points_tr[9:13]:
        
        # initialize point dictionary
        point_dict = {}
        point_dict['point_number'] = point_number

        # point data are in 'td' tags
        point_td = point_tr.select('td')
       
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
                point_dict['receiver']
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
            point_in_game = 'DO THIS'
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
      

        # shots
        shots = []
        point_dict['shots'] = shots
    
        points.append(point_dict)
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

def getMatchLinks(link='http://www.tennisabstract.com/charting/'):
    '''
    Returns list of match links
    '''

    # get BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # match links are in 'p' -> 'a' tags (starting with 3rd)
    match_links = soup.select('p a')[2:]
    match_links = [f"{link}{match_link['href']}" for match_link in match_links]

    return match_links


link = 'http://www.tennisabstract.com/charting/20001118-M-Paris_Masters-SF-Juan_Carlos_Ferrero-Marat_Safin.html'
print(getMatchData(link))
