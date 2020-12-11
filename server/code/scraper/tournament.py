import requests
from bs4 import BeautifulSoup

def getTournamentData(link):
    '''
    Takes in a tournament link and returns a dictionary of tournament data
    '''

    # initialize dictionary
    tournament_dict = {}
    tournament_dict['link'] = link

    # gender
    # tournament name is `.../jstourneys/<name>`
    # if tournament starts with W_ then it's W(omen) else M(en)
    tournament_name = link.split('jstourneys/')[1]
    tournament_dict['gender'] = 'W' if tournament_name.startswith('W_') else 'M'

    # name
    # surface
    # sets

    return tournament_dict

tournament_link = 'http://www.minorleaguesplits.com/tennisabstract/cgi-bin/jstourneys/W_2019Us_Open.js'
tournament_data = getTournamentData(tournament_link)
print(tournament_data)