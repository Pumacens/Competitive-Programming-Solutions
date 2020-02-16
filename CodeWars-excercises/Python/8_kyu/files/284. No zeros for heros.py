def no_boring_zeros(n):
    return int(str(n).rstrip('0')) if n else 0


# def no_boring_zeros(n):
#     try:
#         return int(str(n).rstrip('0'))
#     except ValueError:
#         return 0


# def no_boring_zeros(n):
#     if n==0:
#         return n
#     while n%10==0:
#         n=n/10
#     return n