from models.backhands import BackhandModel
from models.countries import CountryModel
from models.genders import GenderModel
from models.hands import HandModel


def getGenderModel(gender):
    '''
    Takes a gender and queries GenderModel for record
    Return record or create new one if not found
    '''

    gender_model_db = GenderModel.objects(gender=gender).first()
    if gender_model_db:
        return gender_model_db

    gender_id_new = max([gender_model['gender_id'] for gender_model in GenderModel.objects()] or [0]) + 1
    gender_model_new = GenderModel(**{'gender_id': gender_id_new, 'gender': gender})
    gender_model_new.save()

    return gender_model_new


def getHandModel(hand):
    '''
    Takes a hand and queries HandModel for record
    Return record or create new one if not found
    '''

    hand_model_db = HandModel.objects(hand=hand).first()
    if hand_model_db:
        return hand_model_db

    hand_id_new = max([hand_model['hand_id'] for hand_model in HandModel.objects()] or [0]) + 1
    hand_model_new = HandModel(**{'hand_id': hand_id_new, 'hand': hand})
    hand_model_new.save()

    return hand_model_new


def getBackhandModel(backhand):
    '''
    Takes a backhand and queries BackhandModel for record
    Return record or create new one if not found
    '''

    backhand_model_db = BackhandModel.objects(backhand=backhand).first()
    if backhand_model_db:
        return backhand_model_db
    
    backhand_id_new = max([backhand_model['backhand_id'] for backhand_model in BackhandModel.objects()] or [0]) + 1
    backhand_model_new = BackhandModel(**{'backhand_id': backhand_id_new, 'backhand': backhand})
    backhand_model_new.save()

    return backhand_model_new


 def getCountryModel(country):
     '''
     Takes a country and queries CountryModel for record
    Return record or create new one if not found
    '''

    country_model_db = CountryModel.objects(country=country).first()
    if country_model_db:
        return country_model_db

    country_id_new = max([country_model['country_id'] for country_model in CountryModel.objects()] or [0]) + 1
    country_model_new = CountryModel(**{'country_id': country_id_new, 'country': country})
    country_model_new.save()

    return country_model_new


def extractVariableFromText(text, variable):
    '''
    Takes in a blob of text and splits accordingly to return a text value
    '''
    # text is in the format: `.....var [variable] = [data to extract];......`
    # so have to split on 'var [variable] = ' and then on ';'
    # also remove quotes
    variable_str = f"var {variable} = "
    return text.split(variable_str)[1].split(';')[0].replace("'","").replace('"', '')
