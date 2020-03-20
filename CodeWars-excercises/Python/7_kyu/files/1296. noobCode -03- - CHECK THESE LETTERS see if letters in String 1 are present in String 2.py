def letter_check(arr): 
    a, b =  map(set, map(str.lower, arr))
    
    for num in b:
        if num not in a:
            return False
            
    return True



# def letter_check(arr): 
#     a,b = (set(s.lower()) for s in arr)
#     return b <= a