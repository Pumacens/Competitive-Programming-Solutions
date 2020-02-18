from collections import OrderedDict

def remove_duplicate_words(s):
    return ' '.join(OrderedDict.fromkeys(s.split()).keys())


# Funciona a partir de python 3.6 porque los diccionaros ahora son ordenados
# def remove_duplicate_words(s):
#     return ' '.join(dict.fromkeys(s.split()))