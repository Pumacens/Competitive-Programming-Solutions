def divisible_by(numbers, divisor):
    return [num for num in numbers if num%divisor == 0]


# def divisible_by(n,d):
#     return filter(lambda x:x % d == 0, n)