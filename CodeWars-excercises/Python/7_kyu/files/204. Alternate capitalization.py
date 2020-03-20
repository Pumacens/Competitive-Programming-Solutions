def capitalize(s):
    result_string = ''.join(s[indx].upper() if indx % 2 == 0 else s[indx] for indx in range(len(s)))
    return [result_string, result_string.swapcase()]


# def capitalize(s):
#     s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
#     return [s, s.swapcase()]


# def capitalize(s):
#     return [''.join(c if (k + i) % 2 else c.upper() for i, c in enumerate(s)) for k in [0, 1]]