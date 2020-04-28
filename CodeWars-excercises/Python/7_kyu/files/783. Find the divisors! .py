from math import sqrt

def divisors(integer):
    lst = []
    for num in range(2, integer//2+1):
        if integer % num == 0:
            lst.append(num)
            
    return lst if len(lst) > 0 else f'{integer} is prime'



# def divisors(integer):
#   return [n for n in range(2, integer//2+1) if integer % n == 0] or '{} is prime'.format(integer)