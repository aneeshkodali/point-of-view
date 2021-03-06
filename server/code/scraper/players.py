import requests
from bs4 import BeautifulSoup
import ast
import datetime

from models.players import PlayerModel
import scraper.helper as helper

def getPlayerData(link):

    '''
    Takes in a player link and returns a PlayerModel(dictionary of player data)
    '''

    # initialize model
    player_model = PlayerModel()

    # link
    player_model['link'] = link

    # gender
    try:
        gender = 'W' if 'wplayer' in link else 'M'
        gender_model = helper.getGenderModel(gender)
        player_model['gender_id'] = gender_model['gender_id']
    except:
        pass

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # data is in the '4th' <script> tag
    text = str(soup.select('script')[3])

    # full_name
    try:
        full_name = helper.extractVariableFromText(text, 'fullname')
        if full_name:
            player_model['full_name'] = full_name
    except:
        pass

    # height
    try:
        height = helper.extractVariableFromText(text, 'ht')
        if height:
            player_model['height'] = height
    except:
        pass

    try:
        date_of_birth = helper.extractVariableFromText(text, 'dob')
        if date_of_birth:
            year = int(date_of_birth[:4])
            month = int(date_of_birth[4:6])
            day = int(date_of_birth[6:8])
            player_model['date_of_birth'] = datetime.datetime(year, month, day)
    except:
        pass

    # hand
    try:
        hand = helper.extractVariableFromText(text, 'hand')
        hand_model = helper.getHandModel(hand)
        player_model['hand_id'] = hand_model['hand_id']
    except:
        pass

    # backhand
    try:
        backhand = helper.extractVariableFromText(text, 'backhand')
        backhand_model = helper.getBackhandModel(backhand)
        player_model['backhand_id'] = backhand_model['backhand_id']
    except:
        pass

    # country
    try:
        country = helper.extractVariableFromText(text, 'country')
        country_model = helper.getCountryModel(country)
        player_model['country_id'] = country_model['country_id']
    except:
        pass

    # image url
    try:
        photog = helper.extractVariableFromText(text, 'photog')
        full_name = player_model['full_name']
        if photog and full_name:
            player_model['image_url'] = f"http://www.tennisabstract.com/photos/{full_name.lower().replace(' ', '_')}-{photog}.jpg"
    except:
        pass
    

    return player_model


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