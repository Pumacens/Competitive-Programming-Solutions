import re

def get_free_urinals(urinals):
    if bool(re.search(r'1{2,}', urinals)):
        return -1
        
    urinals = list(''.join(['--', urinals, '--']))
    free_urinals = 0
    
    try:
        i = urinals.index('0')
    except ValueError:
        return 0

    for indx in range(i, len(urinals)-2):
        if urinals[indx] == '0' and urinals[indx-1] != '1' and urinals[indx+1] != '1':
            free_urinals += 1
            urinals[indx] = '1' 
            
    return free_urinals



# def get_free_urinals(urinals):
#     return -1 if '11' in urinals else sum(((len(l)-1)//2 for l in f'0{urinals}0'.split('1')))