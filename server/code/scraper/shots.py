from models.shots import ShotModel

def getShotData(rally_list, player_list, result):
    '''
    Given a rally list (where each element is of form: <stroke> <location> <result if any>)
    and player list of server/receiver models (to determine who hit which shot)
    return list of dictionaries of shot data
    '''

    # initialize shots
    shots = []
    
    location_list = ['crosscourt', 'down the line', 'down the middle', 'down the T', 'inside-in', 'inside-out', 'to body', 'wide']
    server = player_list[0]
    receiver = player_list[1]

    # split first element into 1st serve/2nd serve (if exists)
    serve_element = rally_list[0]
    if '2nd serve' in serve_element:
        # remove 1st serve from 1st element (if exists)
        serve_split = serve_element.split('.')
        first_serve = serve_split[0].strip()
        second_serve = serve_split[1].strip()
        rally_list[0] = second_serve

        # create/append 1st serve dictionary
        first_serve_dict = {}
        
        # shot_number
        first_serve_dict['shot_number'] = 1

        # shot_number_w_serve
        first_serve_dict['shot_number_w_serve'] = 1

        # shot_by
        first_serve_dict['shot_by'] = server

        # shot_location
        for location in location_list:
            if location in first_serve:
                first_serve_dict['location'] = location
                break

        # shot
        first_serve_dict['shot'] = '1st serve'

        # result
        first_serve_dict['result'] = 'fault'

        # append to list
        shots.append(first_serve_dict)


    # loop through shots
    for i, shot in enumerate(rally_list):

        # initialize shot_dict
        shot_dict = {}

        # shot_number
        shot_num = i+1
        shot_dict['shot_number'] = shot_num

        # shot_number_w_serve
        shot_dict['shot_number_w_serve'] = len(shots)+1

        # shot_by
        shot_by = server if shot_num % 2 != 0 else receiver
        shot_dict['shot_by'] = shot_by

        # shot_location
        for location in location_list:
            if location in shot:
                shot_dict['location'] = location
                break

        # shot
        shot_shot = shot.split(location)[0].strip()
        shot_dict['shot'] = shot_shot 

        # result
        shot_dict['result'] = result if i == len(rally_list)-1 else 'none'


        # add record
        shot_model = ShotModel(**shot_dict)
        shot_model.save()

