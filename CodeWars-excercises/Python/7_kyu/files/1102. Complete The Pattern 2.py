def pattern(n):
    return '\n'.join(''.join(map(str, list(range(n, i, -1)))) for i in range(n))



# def pattern(n):
#     r = xrange(n, 0, -1)
#     a = [str(i) for i in r]
#     return '\n'.join(''.join(a[:i]) for i in r)