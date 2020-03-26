def seven(m):
    final_num = m
    x = final_num // 10
    y = final_num % 10
    final_num = x - 2*y
    steps = 1
    
    while len(str(final_num)) > 2:
        x = final_num // 10
        y = final_num % 10
        final_num = x - 2*y
        steps += 1

    return (final_num, steps) if m else (0, 0)



# def seven(m, step = 0):
#     if m < 100: return (m, step)
#     x, y, step = m // 10, m % 10, step + 1
#     res = x - 2 * y
#     return seven(res, step)