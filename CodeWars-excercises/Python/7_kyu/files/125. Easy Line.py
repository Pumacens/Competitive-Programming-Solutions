def easyline(n):
    n *= 2
    line = [1]
    for k in range(n):
       line.append(line[k] * (n-k) // (k+1))

    return int(line[len(line)//2])
    

# from math import factorial

# def easyline(n):
#     return factorial(2*n)//(factorial(n)**2)