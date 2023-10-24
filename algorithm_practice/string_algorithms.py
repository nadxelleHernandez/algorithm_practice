def camelcase(s)-> int:
    if not s:
        return 0
    
    words = 1
    for char in s:
        if char.isupper():
            words += 1

    return words

def marsExploration(s):
    '''
    s = SOSSPSSQSSOR

    Expected signal: SOSSOSSOSSOS
    Recieved signal: SOSSPSSQSSOR
    Difference:          X  X   X
    
    returns 3
    '''

    if not s:
        raise ValueError("The string of data is Empty")
    
    s_len = len(s)
    if s_len % 3 != 0:
        raise ValueError("The string of data is incomplete")
    
    help_str = "SOS"
    help_i = 0
    char_changed = 0
    for char in s:
        if help_i == 3:
            help_i = 0
        if char != help_str[help_i]:
            char_changed += 1
        help_i += 1

    return char_changed
