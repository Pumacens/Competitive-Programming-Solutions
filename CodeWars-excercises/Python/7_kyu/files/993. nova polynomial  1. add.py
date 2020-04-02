# return the sum of the two polynomials p1 and p2.  
def poly_add(p1, p2):
    p1 = p1[::]
    p2 = p2[::]

    if len(p1) >= len(p2):
        for indx, value in enumerate(p2):
            p1[indx] += value
            
        return p1
        
    else:
        for indx, value in enumerate(p1):
            p2[indx] += value
        
        return p2



# from itertools import izip_longest
# def poly_add(p1, p2):
#     return [a+b for a, b in izip_longest(p1, p2, fillvalue=0)]


# def poly_add(p1,p2):
#     if p1 == []:
#         return p2
#     if p2 == []:
#         return p1
#     return [p1[0] + p2[0]] + poly_add(p1[1:], p2[1:])