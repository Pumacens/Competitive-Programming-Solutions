# import re

def mouth_size(animal): 
  return 'small' if animal.lower() == "alligator" else 'wide'


# def mouth_size(animal):
#    return 'small' if  re.search('alligator', animal, re.IGNORECASE) else 'wide'


# def mouth_size(animal): 
#     mouth = {'alligator':'small'}
#     return mouth.get(animal.lower(), 'wide')