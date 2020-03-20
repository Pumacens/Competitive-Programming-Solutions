def all_rationals():
#   The value of the left-hand node below a/b is a/a+b
#   The value of the right-hand node below a/b is a+b/b
    value = (1, 1)
    yield (1, 1)
    lst_1 = [(value[0], value[1]+value[0]), (value[1]+value[0], value[1])]
    lst_2 = []
    while True:
        for value in lst_1:
            yield value
            lst_2.append((value[0], value[1]+value[0]))
            lst_2.append((value[1]+value[0], value[1]))
            
        lst_1 = lst_2[::]
        lst_2.clear()



# def all_rationals():
#     yield (1, 1)
#     for a, b in all_rationals():
#         yield from [(a, a + b), (a + b, b)]



# from collections import deque
# def all_rationals():
#     result = deque([(1, 1)])
#     while result:
#         a, b = result.popleft()
#         result += [(a, a + b), (a + b, b)]
#         yield a, b