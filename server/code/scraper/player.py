import requests
from bs4 import BeautifulSoup
import ast

def getPlayerData(link):

    '''
    Takes in a player link and returns a dictionary of player data
    '''

    # initialize dictionary
    player_dict = {}

    player_dict['link'] = link
    player_dict['gender'] = 'W' if 'wplayer' in link else 'M'

    # create BeautifulSoup object
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'lxml')

    # data is in the '4th' <script> tag
    text = str(soup.select('script')[3])

    #### GET VARIABLE DATA

    # easier to create list of dictionaries comprising of <column_name>:<variable_to_look_for_in_text> pairs
    column_variables = [
                        {'column_name': 'full_name', 'variable_name': 'fullname'},
                        {'column_name': 'last_name', 'variable_name': 'lastname'},
                        {'column_name': 'date_of_birth', 'variable_name': 'dob'},
                        {'column_name': 'height', 'variable_name': 'ht'},
                        {'column_name': 'hand', 'variable_name': 'hand'},
                        {'column_name': 'backhand', 'variable_name': 'backhand'},
                        {'column_name': 'country', 'variable_name': 'country'},
                        ]
    # loop through key, value pairs
    for column_variable in column_variables:
        column = column_variable['column_name']
        variable = column_variable['variable_name']

        # if value exists AND value not equal to empty string, add it to dictionary
        try:
            column_value = extractData(text, variable)
            if column_value:
                player_dict[column] = column_value

        except:
            pass

    # get image_url
    # this is outside of loop because it's special: have to check if full_name in dictionary
    try:
        photog = extractData(text, 'photog')
        full_name = player_dict['full_name']
        if photog and full_name:
            player_dict['image_url'] = f"http://www.tennisabstract.com/photos/{full_name.lower().replace(' ', '_')}-{photog}.jpg"
    except:
        pass
    

    return player_dict

def extractData(text, variable):
    '''
    Takes in a blob of text and splits accordingly to return a text value
    '''
    # text is in the format: `.....var [variable] = [data to extract];......`
    # so have to split on 'var [variable] = ' and then on ';'
    # also remove quotes
    variable_str = f"var {variable} = "
    return text.split(variable_str)[1].split(';')[0].replace("'","")


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
        link = f"http://www.tennisabstract.com/cgi-bin/{'w' if gender=='W' else ''}player.cgi?p={name.replace(' ', '')}"
        # append to list
        player_links.append(link)
    
    return player_links