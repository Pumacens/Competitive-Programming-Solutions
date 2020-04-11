def sum_digits(number):
    num = str(number)
    return sum(int(digit) for digit in (num[1:] if '-' in num else num))


# def sum_digits(number):
#     return sum(map(int, str(abs(number))))