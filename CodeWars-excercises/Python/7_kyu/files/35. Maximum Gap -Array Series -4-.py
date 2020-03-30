def max_gap(numbers):
    numbers = sorted(numbers, reverse=True)
    return max(a-b for a,b in zip(numbers, numbers[1:]))



# import numpy
# def max_gap(numbers):
#     return max(numpy.diff(sorted(numbers)))