import requests
from bs4 import BeautifulSoup
import ast
import datetime

from models.backhands import BackhandModel
from models.countries import CountryModel
from models.genders import GenderModel
from models.hands import HandModel
from scraper.helper import extractVariableFromText

def getPlayerData(link):

    '''
    Takes in a player link and returns a dictionary of player data
    '''

    # initialize dictionary
    player_dict = {}

    # link
    player_dict['link'] = link

    # gender_id
    # Either queries genders table for gender_id or creates new record
    try:
        gender = 'W' if 'wplayer' in link else 'M'
        gender_model_db = GenderModel.find_by_gender(gender)
        if gender_model_db:
            player_dict['gender_id'] = gender_model_db.gender_id
        else:
            gender_id_new = max([gender_model['gender_id'] for gender_model in GenderModel.objects()] or [0]) + 1
            gender_dict_new = {'gender_id': gender_id_new, 'gender': gender}
            gender_model_new = GenderModel(**gender_dict_new)
            gender_model_new.save()
            player_dict['gender_id'] = gender_model_new.gender_id
    except:
        pass

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # data is in the '4th' <script> tag
    text = str(soup.select('script')[3])

    #### GET VARIABLE DATA

    # full_name
    try:
        full_name = extractVariableFromText(text, 'fullname')
        if full_name:
            player_dict['full_name'] = full_name
    except:
        pass

    # height
    try:
        height = extractVariableFromText(text, 'ht')
        if height:
            player_dict['height'] = height
    except:
        pass

    try:
        date_of_birth = extractVariableFromText(text, 'dob')
        if date_of_birth:
            year = int(date_of_birth[:4])
            month = int(date_of_birth[4:6])
            day = int(date_of_birth[6:8])
            player_dict['date_of_birth'] = datetime.datetime(year, month, day)
    except:
        pass

    # hand_id
    # Either queries hands table for hand_id or creates new record
    try:
        hand = extractVariableFromText(text, 'hand')
        hand_model_db = HandModel.find_by_hand(hand)
        if hand_model_db:
            player_dict['hand_id'] = hand_model_db.hand_id
        else:
            hand_id_new = max([hand_model['hand_id'] for hand_model in HandModel.objects()] or [0]) + 1
            hand_dict_new = {'hand_id': hand_id_new, 'hand': hand}
            hand_model_new = HandModel(**hand_dict_new)
            hand_model_new.save()
            player_dict['hand_id'] = hand_model_new.hand_id
    except:
        pass

    # backhand_id
    # Either queries backhands table for backhand or creates new record
    try:
        backhand = extractVariableFromText(text, 'backhand')
        backhand_model_db = BackhandModel.find_by_backhand(backhand)
        if backhand_model_db:
            player_dict['backhand_id'] = backhand_model_db.backhand_id
        else:
            backhand_id_new = max([backhand_model['backhand_id'] for backhand_model in BackhandModel.objects()] or [0]) + 1
            backhand_dict_new = {'backhand_id': backhand_id_new, 'backhand': backhand}
            backhand_model_new = BackhandModel(**backhand_dict_new)
            backhand_model_new.save()
            player_dict['backhand_id'] = backhand_model_new.backhand_id
    except:
        pass

    # country_id
    # Either queries countries table for country_id or creates new record
    try:
        country = extractVariableFromText(text, 'country')
        country_model_db = CountryModel.find_by_country(country)
        if country_model_db:
            player_dict['country_id'] = country_model_db.country_id
        else:
            country_id_new = max([country_model['country_id'] for country_model in CountryModel.objects()] or [0]) + 1
            country_dict_new = {'country_id': country_id_new, 'country': country}
            country_model_new = CountryModel(**country_dict_new)
            country_model_new.save()
            player_dict['country_id'] = country_model_new.country_id
    except:
        pass

    # image url
    try:
        photog = extractVariableFromText(text, 'photog')
        full_name = player_dict['full_name']
        if photog and full_name:
            player_dict['image_url'] = f"http://www.tennisabstract.com/photos/{full_name.lower().replace(' ', '_')}-{photog}.jpg"
    except:
        pass
    

    return player_dict


def getPlayerList(link='http://www.minorleaguesplits.com/tennisabstract/cgi-bin/jsplayers/mwplayerlist.js'):

    '''
    Returns array of player names from site
    Each element is of the form `(<gender> <full name>)`
    '''

    # get BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # get list-like string
    # string is of format: `var playerlist=[list];`
    # so split on `playerlist=` and `;`
    player_list_str = soup.text.split('playerlist=')[1].split(';')[0]

    # evaluate as list
    player_list = ast.literal_eval(player_list_str)

    return player_list

def getPlayerLinks():

    '''
    Takes list of players, where each element contains gender and fullname
    Return list of player links that contain player data
    '''

    # get player list from function
    # elements are of the form `(<gender>) <full name>``
    player_list = getPlayerList()

    # initialize list
    player_links = []

    # loop through list
    for player in player_list:
        # extract gender
        gender = player.split('(')[1].split(')')[0]
        #extract name
        name = player.split(') ')[1]
        # construct link
        link = constructPlayerLink(name, gender)
        # append to list
        player_links.append(link)
    
    return player_links


def constructPlayerLink(name, gender, url_stem='http://www.tennisabstract.com/cgi-bin/'):
    '''
    Creates a url for a player based on the args provided
    url is of form: <url_stem><w if women>player.cgi?p=<name>
    '''

    return f"{url_stem}{'w' if gender=='W' else ''}player.cgi?p={name.replace(' ', '')}"