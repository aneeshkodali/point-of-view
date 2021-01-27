import requests
from bs4 import BeautifulSoup
import datetime

from models.players import PlayerModel
from models.tournaments import TournamentModel
frpm models.tournament_names import TournamentNameModel
from scraper.tournament import constructTournamentLink, getTournamentData
from scraper.player import constructPlayerLink, getPlayerData
from scraper.point import getPointTable, getPointData



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
        date = suffix[0]
        if date:
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:])
            match_dict['date'] = datetime.datetime(year, month, day)
    except:
        pass

    # gender_id (not needed as a column)
    # Either queries genders table for gender_id or creates new record
    try:
        gender = suffix[1]
        gender_model_db = GenderModel.find_by_gender(gender)
        if gender_model_db:
            gender_id = gender_model_db.gender_id
        else:
            gender_id_new = max([gender_model['gender_id'] for gender_model in GenderModel.objects()] or [0]) + 1
            gender_dict_new = {'gender_id': gender_id_new, 'gender': gender}
            gender_model_new = GenderModel(**gender_dict_new)
            gender_model_new.save()
            gender_id = gender_model_new.gender_id
    except:
        pass

    # tournament_id
    # Either queries tournament_names table for tournament_name_id or creates new record
    # Then either queries tournaments table for tournament_id or creates new record
    try:
        tournament_name = suffix[2].replace('_', ' ')
        tournament_name_model_db = TournamentNameModel.find_by_name(tournament_name)
        if tournament_name_model_db:
            tournament_name_id = tournament_name_model_db.tournament_name_id
        else:
            tournament_name_dict_new = {'tournament_name': tournament_name}
            tournament_name_model_new = TournamentNameModel(**tournament_name_dict_new)
            tournament_name_model_new.save()
            tournament_name_id = tournament_name_model_new.tournament_name_id

        tournament_model_db = TournamentModel.find_by_name_id_and_gender_id_and_year(tournament_name_id, gender_id, year)
        if tournament_model_db:
            tournament_dict['tournament_id'] = tournament_model_db.tournament_id
        else:
            tournament_link = constructTournamentLink(tournament_name, geder, year)
            tournament_dict_new = getTournamentData(tournament_link)
            tournament_model_new = TournamentModel(**tournament_dict_new)
            tournament_model_new.save()
            tournament_dict['tournament_id'] = tournament_model_new.tournament_id

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
        player_names = [player_one, player_two]
        if player_names:
                players = []
                player_models = []
                for player_name in player_names:
                    player_link = constructPlayerLink(name=player_name, gender=gender)
                    player_db = PlayerModel.find_by_link(player_link)
                    if player_db:
                        players.append(player_db)
                        player_models.append({'player_name': player_name, 'player_model': player_db})
                    else:
                        player_data = getPlayerData(player_link)
                        player_model = PlayerModel(**player_data)
                        player_model.save()
                        players.append(player_model)
                        player_models.append({'player_name': player_name, 'player_model': player_model})
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
        winner_name = result.split(' d.')[0]
        if winner_name:
            winner = players[0] if winner_name == player_names[0] else players[1]
            match_dict['winner'] = winner
    except:
        pass

    # loser
    try:
        loser_name = list(filter(lambda player: player != winner, player_names))[0]
        if loser_name:
            loser = players[1] if winner_name == player_names[0] else players[0]
            match_dict['loser'] = loser
    except:
        pass

    # score
    try:
        score = result.split(f"{loser_name} ")[1]
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
            points_data = getPointData(point_table, player_models)
            match_dict['points'] = points_data
    except:
        pass

    return match_dict


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
