def draw_stairs(n):
    return ''.join('I'.rjust(enter)+'\n' for enter in range(1, n+1))[:-1]



# def draw_stairs(n):
#     return '\n'.join(' '*i+'I' for i in range(n))


# def draw_stairs(n):
#   return '\n'.join('I'.rjust(i + 1) for i in range(n))