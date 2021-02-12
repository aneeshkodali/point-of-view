import requests
from bs4 import BeautifulSoup
import ast
import datetime

from models.levels import LevelModel
from models.surfaces import SurfaceModel
from models.tournaments import TournamentModel
from scraper.helper import extractVariableFromText, getGenderModel, getTournamentNameModel

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
        gender_model = getGenderModel(gender)
        tournament_model['gender'] = gender_model
    except:
        pass

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')
    soup_text = soup.text

    # year
    try:
        year = extractVariableFromText(soup_text, 'tyear')
        if year:
            tournament_model['year'] = year
    except:
        pass

    # tournament_name
    try:
        tournament_name = extractVariableFromText(soup_text, 'tname')
        tournament_name_model = getTournamentNameModel(tournament_name)
        tournament_model['tournament_name'] = tournament_name_model
    except:
        pass
  
    # date
    try:
        date = extractVariableFromText(soup_text, 'tdate')
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
        surface_model_db = SurfaceModel.find_by_surface(surface)
        if surface_model_db:
            tournament_model['surface'] = surface_model_db
        else:
            surface_id_new = max([surface_model['surface_id'] for surface_model in SurfaceModel.objects()] or [0]) + 1
            surface_model_new = SurfaceModel(**{'surface_id': surface_id_new, 'surface': surface})
            surface_model_new.save()
            tournament_model['surface'] = surface_model_new
    except:
        pass
   
    # level
    try:
        level = soup_text.split('var tlev=')[1].split(';')[0].replace("'","").replace('"', '')
        level_model_db = LevelModel.find_by_level(level)
        if level_model_db:
            tournament_model['level'] = level_model_db
        else:
            level_id_new = max([level_model['level_id'] for level_model in LevelModel.objects()] or [0]) + 1
            level_model_new = LevelModel(**{'level_id': level_id_new, 'level': level})
            level_model_new.save()
            tournament_model['level'] = level_model_new
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