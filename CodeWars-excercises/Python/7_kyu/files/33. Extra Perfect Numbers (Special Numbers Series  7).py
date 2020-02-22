def extra_perfect(n):
    return [num for num in range(1, n+1) if bin(num)[2]=='1' and bin(num)[-1]=='1']


# def extra_perfect(n):
#     return range(1, n + 1, 2)


# def extra_perfect(n):
#     return [i for i in range(n+1) if i % 2 != 0] 