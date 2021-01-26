import requests
from bs4 import BeautifulSoup
import ast
import datetime

from models.genders import GenderModel
from scraper.helper import extractVariableFromText
from models.levels import LevelModel
from models.surfaces import SurfaceModel
from models.tournament_names import TournamentNameModel

tournament_base_url = 'http://www.minorleaguesplits.com/tennisabstract/cgi-bin/jstourneys/'

def getTournamentData(link):
    '''
    Takes in a tournament link and returns a dictionary of tournament data
    '''

    # initialize dictionary
    tournament_dict = {}
    tournament_dict['link'] = link

    # tournament name is `.../jstourneys/<name>`
    tournament_name = link.split('jstourneys/')[1]

    # gender_id
    # if tournament starts with W_ then it's W(omen) else M(en)
    try:
        gender = 'W' if tournament_name.startswith('W_') else 'M'
        gender_model_db = GenderModel.find_by_gender(gender)
        if gender_model_db:
            tournament_dict['gender_id'] = gender_model_db.gender_id
        else:
            gender_id_new = max([gender_model['gender_id'] for gender_model in GenderModel.objects()] or [0]) + 1
            gender_dict_new = {'gender_id': gender_id_new, 'gender': gender}
            gender_model_new = GenderModel(**gender_dict_new)
            gender_model_new.save()
            tournament_dict['gender_id'] = gender_model_new.gender_id
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
            tournament_dict['year'] = year
    except:
        pass

    # tournament_name_id
    try:
        tournament_name = extractVariableFromText(soup_text, 'tname')
        tournament_name_model_db = TournamentNameModel.find_by_name(tournament_name)
        if tournament_name_model_db:
            tournament_dict['tournament_name_id'] = tournament_name_model_db.tournament_name_id
        else:
            tournament_name_dict_new = {'name': tournament_name}
            tournament_name_model_new = TournamentNameModel(**tournament_name_dict_new)
            tournament_name_model_new.save()
            tournament_dict['tournament_name_id'] = tournament_name_model_new.tournament_name_id
    except:
        pass
  
    # date
    try:
        date = extractVariableFromText(soup_text, 'tdate')
        if date:
            year = int(date[:4])
            month = int(date[4:6])
            day = int(date[6:8])
            tournament_dict['date'] = datetime.datetime(year, month, day)
    except:
        pass

    # size
    try:
        size = soup_text.split('var tsize=')[1].split(';')[0].replace("'","").replace('"', '')
        if size:
            tournament_dict['size'] = size
    except:
        pass

    # points
    try:
        points = soup_text.split('var tpoints=')[1].split(';')[0].replace("'","").replace('"', '')
        if points:
            tournament_dict['points'] = points
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

    # surface_id
    try:
        surface = soup_text.split('var tsurf=')[1].split(';')[0].replace("'","").replace('"', '').lower()
        surface_model_db = SurfaceModel.find_by_surface(surface)
        if surface_model_db:
            tournament_dict['surface_id'] = surface_model_db.surface_id
        else:
            surface_id_new = max([surface_model['surface_id'] for surface_model in SurfaceModel.objects()] or [0]) + 1
            surface_dict_new = {'surface_id': surface_id_new, 'surface': surface}
            surface_model_new = SurfaceModel(**surface_dict_new)
            surface_model_new.save()
            tournament_dict['surface_id'] = surface_model_new.surface_id
    except:
   
    # level_id
    try:
        level = soup_text.split('var tlev=')[1].split(';')[0].replace("'","").replace('"', '')
        if level:
            level_id = LevelModel.find_by_level(level).level_id
            tournament_dict['level_id'] = level_id
    except:
        pass


    return tournament_dict


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


def constructTournamentLink(year, name, gender, url_stem=tournament_base_url):
    '''
    Creates a url for a tournament based on the args provided
    url is of form: <url_stem><W_ if women tournament><year><name>.js
    '''

    return f"{url_stem}{'W_' if gender == 'W' else ''}{year}{name.replace(' ', '_')}.js"