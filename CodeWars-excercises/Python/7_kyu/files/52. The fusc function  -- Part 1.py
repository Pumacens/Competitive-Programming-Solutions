def fusc(n):
    if n in (0, 1):
        return n
    
    elif n%2==0:
        return fusc(n//2)
        
    else:
        n = (n - 1) // 2
        return fusc(n) + fusc(n + 1)


