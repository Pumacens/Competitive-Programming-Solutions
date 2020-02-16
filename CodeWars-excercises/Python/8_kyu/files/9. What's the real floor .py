def get_real_floor(n):
    return n if n <= 0 else n - (1 if n < 13 else 2)


# def get_real_floor(n):
#     if n <= 0: return n
#     if n < 13: return n-1
#     if n > 13: return n-2