from itertools import cycle

def how_much_i_love_you(nb_petals):
    
    cont = 0
    for _ in cycle((1, 2, 3, 4, 5, 6)):
        indx = _
        cont += 1
        if cont == nb_petals:
            break
        
    return {1: 'I love you',
            2: 'a little',
            3: 'a lot',
            4: 'passionately',
            5: 'madly',
            6: 'not at all'
            }[indx]