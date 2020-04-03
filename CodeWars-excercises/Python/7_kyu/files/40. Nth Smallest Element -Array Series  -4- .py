from heapq import nsmallest

def nth_smallest(arr, pos):
    return nsmallest(pos, arr)[-1]



# def nth_smallest(arr, pos):
#     return sorted(arr)[pos-1]