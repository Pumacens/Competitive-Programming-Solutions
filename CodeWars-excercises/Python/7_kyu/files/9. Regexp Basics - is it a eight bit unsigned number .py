def eight_bit_number(n):
    return n in map(str, range(256))



# import re
# def eight_bit_number(n):
#     return bool(re.fullmatch(r"([1-9]?|1\d|2[0-4])\d|25[0-5]", n))



# def eight_bit_number(n):
#     try:        
#         return int(n)>=0 and int(n)<256 and str(int(n))==n
#     except Exception as e:
#         return False