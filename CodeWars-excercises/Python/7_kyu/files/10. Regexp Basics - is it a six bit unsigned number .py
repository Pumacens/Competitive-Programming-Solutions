def six_bit_number(n):
    return n in map(str, range(64))



# import re
# def six_bit_number(s):
#     return bool(re.match(r'([1-5]?\d|6[0-3])\Z',s))