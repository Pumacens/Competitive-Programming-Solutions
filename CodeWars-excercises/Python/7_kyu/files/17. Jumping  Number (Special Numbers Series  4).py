def jumping_number(number):
    number = str(number)
    
    for i in range(len(number)-1):
        if abs(int(number[i]) - int(number[i+1])) != 1:
            return "Not!!"
            
    return "Jumping!!"



# def jumping_number(number):
#     arr = list(map(int, str(number)))
#     return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]



# def jumping_number(number):
#     digits = [int(char) for char in str(number)]
#     if len(digits) == 1:
#         return 'Jumping!!'
#     else:
#         deltas = (abs(x - y) for x, y in zip(digits, digits[1:]))
#         return 'Jumping!!' if all(delta == 1 for delta in deltas) else 'Not!!'