from heapq import (nlargest, nsmallest)

def min_sum(arr):
    len_arr_by2 = len(arr)//2
    return sum(a*b for a,b in zip(nlargest(len_arr_by2, arr), nsmallest(len_arr_by2, arr)))



# def min_sum(arr):
#     arr = sorted(arr)
#     return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))


