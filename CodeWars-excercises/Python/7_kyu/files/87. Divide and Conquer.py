def div_con(x):
    result = 0
    for value in x:
        if isinstance(value, str):
            result -= int(value)
            
        else:
            result += value
            
    return result



# def div_con(lst):
# return sum(n if isinstance(n, int) else -int(n) for n in lst)