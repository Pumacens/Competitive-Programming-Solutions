from math import pi
def sort_by_area(seq): 
    return sorted(seq, key= lambda x: pi*x*x if type(x) in (int, float) else x[0]*x[1])



