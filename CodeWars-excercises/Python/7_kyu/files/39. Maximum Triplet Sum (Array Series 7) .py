def max_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])


# from heapq import nlargest

# def max_tri_sum(numbers):
#     return sum(nlargest(3, set(numbers)))