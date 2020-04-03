def dominator(arr):
    for possible_dom in set(arr):
        if arr.count(possible_dom) > len(arr)//2:
            return possible_dom
            
    return -1


# from collections import Counter
# def dominator(arr):
#     if not arr:
#         return -1
#     k, v = Counter(arr).most_common(1)[0]
#     return k if v > len(arr) / 2 else -1



# def dominator(arr):
#     return next((x for x in set(arr) if arr.count(x) > len(arr)/2),-1)