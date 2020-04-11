# No usar eval sin verificar el input porque
# calculate("__import__('os').system('rm / -rf --no-preserve-root')")

def calculate(s):
    return str(eval(s.replace('plus', '+').replace('minus', '-')))


# def calculate(s):
#     return str(sum(int(n) for n in s.replace("minus", "plus-").split("plus")))