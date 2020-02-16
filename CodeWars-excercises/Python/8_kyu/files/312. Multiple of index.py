def multiple_of_index(arr):
    lst = []
    
    for indx in range(1, len(arr)):
        if arr[indx] % indx == 0:
            lst.append(arr[indx])
            
    return lst


# def multiple_of_index(l):
#     return [l[i] for i in range(1, len(l)) if l[i] % i == 0]