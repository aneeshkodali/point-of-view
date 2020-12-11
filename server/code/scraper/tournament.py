import requests
from bs4 import BeautifulSoup
import ast

from helper import extractVariableFromText


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

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')
    soup_text = soup.text

    # name
    try:
        name = extractVariableFromText(soup_text, 'tname')
        if name:
            tournament_dict['name'] = name
    except:
        pass

    # surface
    try:
        surface = soup_text.split('var tsurf=')[1].split(';')[0].replace("'","").replace('"', '')
        if surface:
            tournament_dict['surface'] = surface
    except:
        pass

    # sets
    # sets is a list-like string: ['All', '2 Sets', '3 Sets', ..., 'RET', 'W/O']
    # goal is to convert to list, only include elements with 'Sets' in string, then extract the last element integer
    try:
        sets_list_str = soup_text.split('var schoices=')[1].split(';')[0]
        sets_list = ast.literal_eval(sets_list_str)
        sets_list = [elem.split(' Sets')[0] for elem in sets_list if ' Sets' in elem]
        sets_num = sets_list[-1]
        if sets_num:
            tournament_dict['sets'] = sets_num
    except:
        pass

    return tournament_dict
