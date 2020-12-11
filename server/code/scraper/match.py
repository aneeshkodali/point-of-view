import requests
from bs4 import BeautifulSoup
import datetime

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
    points = []
    match_dict['points'] = points

    return match_dict

link = 'http://www.tennisabstract.com/charting/20001118-M-Paris_Masters-SF-Juan_Carlos_Ferrero-Marat_Safin.html'
print(getMatchData(link))