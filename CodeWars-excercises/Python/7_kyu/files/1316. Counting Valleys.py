from math import ceil

def counting_valleys(s):
    s = s.replace('F', '')
    dicc = {'U': 1,
            'D': -1}
            
    has_been_negative = False
    valleys = 0
    count = 0
    
    for move in s:
        count += dicc[move]
        if count < 0:
            has_been_negative = True
            
        if count == 0 and has_been_negative:
            valleys += 1
            has_been_negative = False
                
    return valleys
    