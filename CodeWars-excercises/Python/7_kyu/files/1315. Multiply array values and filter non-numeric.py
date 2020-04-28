def multiply_and_filter(seq, multiplier): 
    return [ value*multiplier for value in seq if isinstance(value, float) or isinstance(value, int) and not isinstance(value, bool)]


# def multiply_and_filter(seq, multiplier): 
#     return [num * multiplier for num in seq if type(num) in (int, float)]