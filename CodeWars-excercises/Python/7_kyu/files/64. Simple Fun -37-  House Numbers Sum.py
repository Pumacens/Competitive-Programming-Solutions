def house_numbers_sum(inp):
    return sum(inp[:inp.index(0)])



# from itertools import takewhile; house_numbers_sum = lambda arr: sum(x for x in takewhile(lambda x: x!=0, arr))


# from itertools import takewhile
# def house_numbers_sum(inp):
    # return sum(takewhile(bool,inp))