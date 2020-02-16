def digitize(n):
    return [int(num) for num in str(n)[::-1]]
    
# clever
# def digitize(n):
#     return map(int, str(n)[::-1])