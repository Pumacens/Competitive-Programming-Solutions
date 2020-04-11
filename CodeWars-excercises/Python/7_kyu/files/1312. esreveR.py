def reverse(lst):
    my_lst = list.copy(lst)
    
    def reverse_generator(internal_lst):
        for i in range(len(internal_lst)-1, -1, -1):
            yield internal_lst[i]
            
    return list(reverse_generator(my_lst))



# from collections import deque
# def reverse(lst):
#     q = deque()
#     for x in lst:
#         q.appendleft(x)
#     return list(q)


# def reverse(lst):
#     out=list(lst)
#     for i in range(len(lst)):
#         out[i] = lst[len(lst)-i-1]
#     return out