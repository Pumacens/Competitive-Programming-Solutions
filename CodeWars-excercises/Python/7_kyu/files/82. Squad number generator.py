from itertools import product
import string

DICC = {2: [11], 
        3: [12, 21], 
        4: [13, 22, 31], 
        5: [14, 23, 32, 41], 
        6: [15, 24, 33, 42, 51], 
        7: [16, 25, 34, 43, 52, 61], 
        8: [17, 26, 35, 44, 53, 62, 71],
        9: [18, 27, 36, 45, 54, 63, 72, 81], 
        10: [19, 28, 37, 46, 55, 64, 73, 82, 91], 
        11: [29, 38, 47, 56, 65, 74, 83, 92], 
        12: [39, 48, 57, 66, 75, 84, 93],
        13: [49, 58, 67, 76, 85, 94], 
        14: [59, 68, 77, 86, 95], 
        15: [69, 78, 87, 96], 
        16: [79, 88, 97], 
        17: [89, 98], 
        18: [99]}


def generate_number(squad, n):
    if n not in squad:
        return n

    if n not in DICC:
        return None

    for two_digit_sol in DICC[n]:
        if two_digit_sol not in squad:
            return two_digit_sol

    return None




# def generate_number(lst, n):
#     lst = set(lst)
#     return (n if n not in lst else
#             next( (9*d+n for d in range(1,10) if 0<n-d<10 and 9*d+n not in lst), None))
