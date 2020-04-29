def sum_even_numbers(seq): 
    return sum(num for num in seq if num%2==0)


def sum_even_numbers(seq): 
    return sum(filter(lambda n: n%2==0, seq))