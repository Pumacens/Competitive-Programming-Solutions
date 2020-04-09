def show_sequence(n):
    if n==0:
        return '0=0'
        
    elif n<0:
        return f'{n}<0'
        
    else:        
        sum_sequence = '+'.join(map(str, range(n+1)))
        return f'{sum_sequence} = {eval(sum_sequence)}'
        


# def show_sequence(n):
#     if n == 0:
#         return "0=0"
#     return "{} = {}" .format("+".join(map(str,range(n+1))),sum(range(n+1))) if n > 0 else "{}<0".format(n)