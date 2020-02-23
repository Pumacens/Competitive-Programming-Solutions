from itertools import chain

def pendulum(values):
    values = sorted(values)
    return list(chain(values[2::2][::-1], [values[0]], values[1::2]))



# def pendulum(a):
#     a = sorted(a)
#     return a[::2][::-1] + a[1::2]



# from collections import deque
# def pendulum(values):
#     x = deque()
#     v = sorted(values)
#     for i, n in enumerate(v):
#         x.append(n) if i%2 else x.appendleft(n)
#     return list(x)