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


def extractVariableFromText(text, variable):
    '''
    Takes in a blob of text and splits accordingly to return a text value
    '''
    # text is in the format: `.....var [variable] = [data to extract];......`
    # so have to split on 'var [variable] = ' and then on ';'
    # also remove quotes
    variable_str = f"var {variable} = "
    return text.split(variable_str)[1].split(';')[0].replace("'","").replace('"', '')
