def max_multiple(divisor, bound):
    for n in range(bound, divisor, -1):
        if n % divisor == 0:
            return n


def max_multiple(divisor, bound):
    return bound - (bound % divisor)


def max_multiple(divisor, bound):
    return bound // divisor * divisor