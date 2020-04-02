from itertools import combinations

def int_diff(arr, n):
    return sum(abs(a-b)==n for a, b in combinations(arr, 2))



# def int_diff(arr, n):
#     num=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if abs(arr[i]-arr[j])==n:
#                 num+=1
#     return num


