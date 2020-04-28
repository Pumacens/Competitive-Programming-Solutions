def halving_sum(n): 
    _sum = 0
    while n >= 1:
        _sum += n
        n //= 2
    
    return _sum


def halving_sum(n): 
    return n and n + halving_sum(n>>1)