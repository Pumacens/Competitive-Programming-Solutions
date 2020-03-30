import heapq
from functools import reduce
import operator

def max_product(lst, n_largest_elements):
    return reduce(operator.mul, heapq.nlargest(n_largest_elements, lst))


# def max_product(lst, n_largest_elements):
#     lst_largest = sorted(lst)[-n_largest_elements:]
#     prod = 1
#     for number in lst_largest:
#         prod *= number
#     return prod



# def max_product(lst, n):
#     from functools import reduce
#     return reduce(lambda x,y: x*y, sorted(lst, reverse=True)[:n])