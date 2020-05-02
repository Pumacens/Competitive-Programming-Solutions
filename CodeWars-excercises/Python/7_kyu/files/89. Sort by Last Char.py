def last(x):
    return sorted(x.split(), key=lambda x: x[-1])


# from operator import itemgetter
# def last(s):
#     return sorted(s.split(), key=itemgetter(-1))