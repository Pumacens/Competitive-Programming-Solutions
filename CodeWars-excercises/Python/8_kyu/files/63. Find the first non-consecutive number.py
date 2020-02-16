def first_non_consecutive(arr):
    if len(arr) <= 1:
        return None
        
    for indx, val in enumerate(range(arr[0], arr[-1]+1, 1 if arr[0] >= 0 else 1)):
        if arr[indx] != val:
            return arr[indx]




# def first_non_consecutive(a):
#     i = a[0]
#     for e in a:
#         if e != i:
#             return e
#         i += 1
#     return None