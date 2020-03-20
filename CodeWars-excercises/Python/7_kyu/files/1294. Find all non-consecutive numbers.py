def all_non_consecutive(arr):
    result = []
    
    for indx in range(1, len(arr)):
        if arr[indx] - arr[indx-1] != 1:
            result.append({'i': indx, 'n': arr[indx]})
        
    return result



# def all_non_consecutive(a):
#     return [{"i": i, "n": y} for i, (x, y) in enumerate(zip(a, a[1:]), 1) if x != y - 1]