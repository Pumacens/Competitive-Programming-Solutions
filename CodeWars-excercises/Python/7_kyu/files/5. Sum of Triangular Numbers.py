def sum_triangular_numbers(n):
    return sum(sum(range(i)) for i in range(2, n+2))


# def sum_triangular_numbers(n):
#     return n*(n+1)*(n+2)/6 if n>0 else 0