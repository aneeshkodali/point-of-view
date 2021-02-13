import requests
from bs4 import BeautifulSoup
import ast
import datetime

from models.tournaments import TournamentModel
import scraper.helper as helper

tournament_base_url = 'http://www.minorleaguesplits.com/tennisabstract/cgi-bin/jstourneys/'

def getTournamentData(link):
    '''
    Takes in a tournament link and returns a TournamentModel(dictionary of tournament data)
    '''

    # initialize model
    tournament_model = TournamentModel()
    tournament_model['link'] = link

    # tournament name is `.../jstourneys/<name>`
    tournament_name = link.split('jstourneys/')[1]

    # gender
    try:
        gender = 'W' if tournament_name.startswith('W_') else 'M'
        gender_model = helper.getGenderModel(gender)
        tournament_model['gender'] = gender_model
    except:
        pass

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')
    soup_text = soup.text

    # year
    try:
        year = helper.extractVariableFromText(soup_text, 'tyear')
        if year:
            tournament_model['year'] = year
    except:
        pass

    # tournament_name
    try:
        tournament_name = helper.extractVariableFromText(soup_text, 'tname')
        tournament_name_model = helper.getTournamentNameModel(tournament_name)
        tournament_model['tournament_name'] = tournament_name_model
    except:
        pass
  
    # date
    try:
        date = helper.extractVariableFromText(soup_text, 'tdate')
        if date:
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:8])
            tournament_model['date'] = datetime.datetime(year, month, day)
    except:
        pass

    # size
    try:
        size = soup_text.split('var tsize=')[1].split(';')[0].replace("'","").replace('"', '')
        if size:
            tournament_model['size'] = size
    except:
        pass

    # points
    try:
        points = soup_text.split('var tpoints=')[1].split(';')[0].replace("'","").replace('"', '')
        if points:
            tournament_model['points'] = points
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
            tournament_model['sets'] = sets_num
    except:
        pass

    # surface
    try:
        surface = soup_text.split('var tsurf=')[1].split(';')[0].replace("'","").replace('"', '').lower()
        surface_model = helper.getSurfaceModel(surface)
        tournament_model['surface'] = surface_model
    except:
        pass
   
    # level
    try:
        level = soup_text.split('var tlev=')[1].split(';')[0].replace("'","").replace('"', '')
        level_model = helper.getLevelModel(level)
        tournament_model['level'] = level_model
    except:
        pass


    return tournament_model


def getTournamentLinks(link=tournament_base_url):
    '''
    Returns array of tournament links
    '''

    # get BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # tournament links are 'a' tags that end in '.js'
    tournament_links = soup.select('a')
    tournament_links = [f"{link}{tournament.text}" for tournament in tournament_links if tournament.text.endswith('.js')]

    return tournament_links


def constructTournamentLink(name, gender, year, url_stem=tournament_base_url):
    '''
    Creates a url for a tournament based on the args provided
    url is of form: <url_stem><W_ if women tournament><year><name>.js
    '''

    return f"{url_stem}{'W_' if gender == 'W' else ''}{year}{name.replace(' ', '_')}.js"