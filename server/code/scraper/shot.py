def getShotData(rally_list, player_list):
    '''
    Given a rally list (where each element is of form: <stroke> <location> <result if any>)
    and player list of server/receiver (to determine who hit which shot)
    return list of dictionaries of shot data
    '''

    # initialize shots
    shots = []
    
    location_list = ['crosscourt', 'down the line', 'down the middle', 'down the T', 'inside-in', 'inside-out', 'to body' 'wide']
    server = player_list[0]
    receiver = player_list[1]

    # loop through shots
    for i, shot in enumerate(rally_list):

        # initialize shot_dict
        shot_dict = {}

        # shot_num
        shot_num = i+1
        shot_dict['shot_num'] = shot_num

        # shot_num_w_serve
        shot_dict['shot_num_w_serve'] = shot_num

        # shot_by
        shot_by = server if shot_num % 2 != 0 else receiver
        shot_dict['shot_by'] = shot_by

        # append to list
        shots.append(shot_dict)

    return shots