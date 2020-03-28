def disarium_number(number):
    return "Disarium !!" if number == sum(int(digit)**position for position, digit in enumerate(str(number), 1)) else "Not !!"


# from itertools import count
# def disarium_number(number):
#     return ('Not !!', 'Disarium !!')[number == sum(map(pow, map(int, str(number)), count(1)))]