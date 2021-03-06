import requests
from bs4 import BeautifulSoup
import datetime

import scraper.helper as helper
from models.match_players import MatchPlayerModel
from models.matches import MatchModel
from scraper.tournaments import constructTournamentLink
from scraper.players import constructPlayerLink
from scraper.points import getPointData

url_stem = 'http://www.tennisabstract.com/charting/'

def getMatchData(link):

    '''
    Takes in a match link and returns a MatchModel(dictionary of match data)
    '''

    # initialize match model
    match_model = MatchModel()
    match_model['link'] = link

    # parse link for data
    # after the stem, link is of the form <date>-<gender>-<tournament>-<round>-<player1>-<player2>.html
    match_suffix = link.split(url_stem)[1].replace('.html','')
    match_model['suffix'] = match_suffix

    suffix = match_suffix.split('-')

    # date
    try:
        date = suffix[0]
        if date:
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:])
            match_model['date'] = datetime.datetime(year, month, day)
    except:
        pass

    # gender (not needed as a column; needed for TournamentModel and PlayerModel)
    try:
        gender = suffix[1]
    except:
        pass

    # tournament
    try:
        tournament_name = suffix[2].replace('_', ' ')
        tournament_link = constructTournamentLink(tournament_name, gender, year)
        tournament_model = helper.getTournamentModel(tournament_link)
        match_model['tournament_id'] = tournament_model['tournament_id']
    except:
        pass

    # round
    try:
        round_name = suffix[3]
        round_model = helper.getRoundModel(round_name)
        match_model['round_id'] = round_model['round_id']
    except:
        pass

    # get BeautifulSoup object
    try:
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'lxml')
    except:
        pass

    # name
    try:
        name = soup.select('h2')[0].text
        if name:
            match_model['name'] = name
    except:
        pass

    # score, sets, match_players
    try:
        player_id_dict = {}

        player_one_name = suffix[4].replace('_', ' ')
        player_one_link = constructPlayerLink(player_one_name, gender)
        player_one_id = helper.getPlayerModel(player_one_link)['player_id']
        player_id_dict[player_one_name] = player_one_id

        player_two_name = suffix[5].replace('_', ' ')
        player_two_link = constructPlayerLink(player_two_name, gender)
        player_two_id = helper.getPlayerModel(player_two_link)['player_id']
        player_id_dict[player_two_name] = player_two_id

        result = soup.select('b')[0].text
        
        winner_name = result.split(' d.')[0]
        loser_name = player_one_name if  winner_name != player_one_name else player_two_name
        winner_id = player_one_id if winner_name == player_one_name else player_two_id
        loser_id = player_one_id if winner_name != player_one_name else player_two_id
        
        score_winner = result.split(f"{loser_name} ")[1]
        sets = len(score_winner.split(' '))

        if result:
            score_loser = ' '.join([f"{x.split('-')[1]}-{x.split('-')[0]}" for x in score_winner.split(' ')])
            match_model['sets'] = sets
            MatchPlayerModel(**{'match_id': match_model['match_id'], 'player_id': winner_id, 'score': score_winner, 'win': 1}).save()
            MatchPlayerModel(**{'match_id': match_model['match_id'], 'player_id': loser_id, 'score': score_loser, 'win': 0}).save()

    except:
        pass

    # point-related data
    getPointData(soup, match_model['match_id'], player_id_dict)
        

    return match_model


def getMatchLinks(link=url_stem):
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




  # points
    #try:
    #    point_table = getPointTable(soup)
    #    if point_table:
    #        points_data = getPointData(point_table, player_models)
    #        match_model['points'] = points_data
    #except:
    #    pass