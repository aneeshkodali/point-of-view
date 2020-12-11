def extractVariableFromText(text, variable):
    '''
    Takes in a blob of text and splits accordingly to return a text value
    '''
    # text is in the format: `.....var [variable] = [data to extract];......`
    # so have to split on 'var [variable] = ' and then on ';'
    # also remove quotes
    variable_str = f"var {variable} = "
    return text.split(variable_str)[1].split(';')[0].replace("'","").replace('"', '')
