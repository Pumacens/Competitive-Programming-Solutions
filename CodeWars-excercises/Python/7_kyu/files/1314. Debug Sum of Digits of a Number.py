def get_sum_of_digits(num):
    _sum = 0
    digits = list(str(num))
    for x in digits:
        _sum += int(x)
        
    return _sum



# def get_sum_of_digits(num):
#     return sum(map(int, str(num)))