def one(sq, fun): 
    return sum(fun(item) for item in sq) == 1



# def one(sq, fun):
#     return True if [fun(v) for v in sq].count(True)==1 else False