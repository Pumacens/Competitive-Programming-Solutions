def array_leaders(numbers):        
    return [leader for indx, leader in enumerate(numbers) if sum(numbers[indx+1:]) < leader]


# def array_leaders(numbers):
#     ret = []
#     _sum = sum(numbers)
#     for n in numbers:
#         _sum -= n
#         if(n>_sum):
#             ret.append(n)
#     return ret