def find_longest(string):
    return sorted(map(len, string.split(' ')))[-1]


# def find_longest(strng):
#     return max(len(a) for a in strng.split())