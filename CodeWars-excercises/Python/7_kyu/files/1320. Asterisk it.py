from collections import deque

def asterisc_it(n):
    if type(n) not in (str, int):
        n = ''.join(str(num) for num in n)
    
    
    len_n = len(str(n))
    n = list(map(int, str(n)))    
    _n = deque(n)
    
    i = 1
    pos_to_insert = 1
    
    while i < len_n:
        if n[i-1]%2==0 and n[i]%2==0:
            _n.insert(pos_to_insert, '*')
            pos_to_insert += 1
            
        i += 1
        pos_to_insert += 1
    
    _n = ''.join(str(num) for num in _n)
    
    return _n


# import re
# def asterisc_it(s):
#     if   isinstance(s,int):  s=str(s)
#     elif isinstance(s,list): s=''.join(map(str,s))
#     return re.sub(r'(?<=[02468])(?=[02468])', '*', s)

