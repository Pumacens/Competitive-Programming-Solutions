import re

def hydrate(drink_string):
    glass_watter = sum(map(int, re.findall(r'\d', drink_string)))
    return f"{glass_watter} glass{'es'*(glass_watter!=1)} of water"



# def hydrate(drink_string): 
#     n_drinks = sum([int(x) for x in drink_string.split(' ') if len(x)==1])
#     return "1 glass of water" if n_drinks == 1 else f"{n_drinks} glasses of water"