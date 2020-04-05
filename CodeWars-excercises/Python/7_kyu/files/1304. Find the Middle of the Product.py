import re
from functools import reduce
from operator import mul


def find_middle(s):
    try:
        digits = map(int, re.findall(r'\d', s))
        num = str(reduce(mul, digits))
        len_num = len(num)
        len_half = len_num//2
        
        return int(num[ len_half - (len_num%2==0) : len_half + 1])
    
    except TypeError:
        return -1




# from operator import mul
# from functools import reduce

# def find_middle(s):
#     if not s or not isinstance(s,str): return -1
    
#     lstDig = [int(c) for c in s if c.isnumeric()]
#     if not lstDig: return -1
    
#     prod = str( reduce(mul,lstDig) )
#     i    = (len(prod) - 1) // 2
#     return int(prod[i:-i or len(prod)])
