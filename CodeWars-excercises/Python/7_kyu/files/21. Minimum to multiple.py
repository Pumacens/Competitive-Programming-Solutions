def minimum(a, x):
    if a <= x:
        return min(x-a, a)
        
    limit = ((x * 2) % (x + 1)) / 2
    result = (a % x)
    
    if (a % x) > limit:
        return x - result
        
    return result



# def minimum(a, x):
#     return min(a % x, -a % x)