def is_very_even_number(n):
    n = str(n)
    
    while len(n) > 1:
        n = str(sum(map(int, str(n))))
    
    return  int(n) % 2 == 0