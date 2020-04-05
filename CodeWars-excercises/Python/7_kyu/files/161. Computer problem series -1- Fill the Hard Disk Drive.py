def save(sizes, hd): 
    num_files = 0
    sum_size = 0
    for file in sizes:
        sum_size += file
        num_files += 1
        if sum_size >= hd:
            return num_files - (sum_size > hd)
            
    return num_files
    


# def save(sizes, hd): 
#     for i,s in enumerate(sizes):
#         if hd < s: return i
#         hd -= s
#     return len(sizes)


# from itertools import *
# def save(sizes, hd): 
#     return sum(1 for _ in takewhile(hd.__ge__, accumulate(sizes)))