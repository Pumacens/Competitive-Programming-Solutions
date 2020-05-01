import string
def switcher(arr):
    dicc = {let:num for let, num in enumerate(string.ascii_lowercase[::-1] + '!? ', 1)}
    return ''.join(dicc[int(value)] for value in arr)



# import string
# letters = string.ascii_lowercase[::-1] + '!? '
# def switcher(arr):
#     return ''.join([letters[ch-1] for ch in map(int, arr) if ch])