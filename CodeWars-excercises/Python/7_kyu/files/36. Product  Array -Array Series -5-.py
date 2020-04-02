from functools import reduce
from operator import mul

def product_array(numbers):
    lst = numbers[::]
    for indx in range(len(lst)):
        lst[indx] = reduce(mul, numbers[:indx]+numbers[indx+1:])
        
    return lst



# from operator import mul
# from functools import reduce

# def product_array(numbers):
#     tot = reduce(mul,numbers)
#     return [tot//n for n in numbers]



# def product_array(n):
#     prod = eval("*".join(map(str,n)))
#     return [prod//i for i in n]