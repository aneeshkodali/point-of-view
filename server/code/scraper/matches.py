import requests
from bs4 import BeautifulSoup
import datetime

from models.match_players import MatchPlayerModel
from models.matches import MatchModel
import scraper.helper as helper
from scraper.tournaments import constructTournamentLink
from scraper.players import constructPlayerLink
#from scraper.points import getPointTable, getPointData

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
    suffix = link.split(url_stem)[1].split('-')

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
        match_model['tournament'] = tournament_model
    except:
        pass

    # round
    try:
        round_name = suffix[3]
        round_model = helper.getRoundModel(round_name)
        match_model['match_round'] = round_model
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
        player_dict = {}

        player_one_name = suffix[4].replace('_', ' ')
        player_one_link = constructPlayerLink(player_one_name, gender)
        player_one_model = helper.getPlayerModel(player_one_link)
        player_dict[player_one_name] = player_one_model

        player_two_name = suffix[5].replace('_', ' ').replace('.html','')
        player_two_link = constructPlayerLink(player_two_name, gender)
        player_two_model = helper.getPlayerModel(player_two_link)
        player_dict[player_two_name] = player_two_model

        result = soup.select('b')[0].text
        
        winner_name = result.split(' d.')[0]
        loser_name = player_one_name if  winner_name != player_one_name else player_two_name
        winner_model = player_one_model if winner_name == player_one_name else player_two_model
        loser_model = player_one_model if winner_name != player_one_name else player_two_model
        
        score = result.split(f"{loser_name} ")[1]
        sets = len(score.split(' '))

        if result:
            match_model['score'] = score
            match_model['sets'] = sets
            MatchPlayerModel(**{'match': match_model, 'player': winner_model, 'win': 1}).save()
            MatchPlayerModel(**{'match': match_model, 'player': loser_model, 'win': 0}).save()

    except:
        pass

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


   # player1 and player2
    #try:
    #    player_one = suffix[4].replace('_', ' ')
    #    player_two = suffix[5].replace('_', ' ').replace('.html','')
    #    player_names = [player_one, player_two]
    #    if player_names:
    #            players = []
    #            player_models = []
    #            for player_name in player_names:
    #                player_link = constructPlayerLink(name=player_name, gender=gender)
    #                player_db = PlayerModel.find_by_link(player_link)
    #                if player_db:
    #                    players.append(player_db)
    #                    player_models.append({'player_name': player_name, 'player_model': player_db})
    #                else:
    #                    player_data = getPlayerData(player_link)
    #                    player_model = PlayerModel(**player_data)
    #                    player_model.save()
    #                    players.append(player_model)
    #                    player_models.append({'player_name': player_name, 'player_model': player_model})
    #            match_model['players'] = players
    #except:
    #    pass

       # winner
    #try:
    #    winner_name = result.split(' d.')[0]
    #    if winner_name:
    #        winner = players[0] if winner_name == player_names[0] else players[1]
    #        match_model['winner'] = winner
    #except:
    #    pass

    ## loser
    #try:
    #    loser_name = list(filter(lambda player: player != winner, player_names))[0]
    #    if loser_name:
    #        loser = players[1] if winner_name == player_names[0] else players[0]
    #        match_model['loser'] = loser
    #except:
    #    pass

    ## score
    #try:
    #    score = result.split(f"{loser_name} ")[1]
    #    if score:
    #        match_model['score'] = score
    #except:
    #    pass

    ## sets
    #try:
    #    sets = score.split(' ')
    #    if sets:
    #        match_model['sets'] = len(sets)
    #except:
    #    pass

  # points
    #try:
    #    point_table = getPointTable(soup)
    #    if point_table:
    #        points_data = getPointData(point_table, player_models)
    #        match_model['points'] = points_data
    #except:
    #    pass