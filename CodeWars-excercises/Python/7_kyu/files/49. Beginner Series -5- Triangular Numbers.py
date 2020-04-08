def is_triangular(t):
    t = int(t)
    return any((n*(n+1)/2)==t for n in range(t+1))



# def is_triangular(t):
#     x = int((t*2)**0.5)
#     return t == x*(x+1)/2
