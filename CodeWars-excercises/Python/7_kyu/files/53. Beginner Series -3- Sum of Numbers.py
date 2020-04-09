def get_sum(a,b):
    if a > b:
        a,b = b, a
        
    return sum(range(a, b+1))



# def get_sum(a,b):
#     if a > b : a,b = b,a
#     return (a+b)*(b-a+1)/2