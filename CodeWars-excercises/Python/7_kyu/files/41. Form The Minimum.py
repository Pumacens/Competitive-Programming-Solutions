def min_value(digits):
     return int("".join(map(str,sorted(set(digits)))))



# def minValue(arr):
#     n = 0
#     for i in sorted(set(arr)):
#         n *= 10
#         n += i
#     return n