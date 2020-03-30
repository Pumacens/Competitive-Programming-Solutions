def special_number(number):
    return "Special!!" if all(digit in {'0', '1', '2', '3', '4', '5'} for digit in str(number)) else "NOT!!"



# def special_number(n):
#     return "Special!!" if max(str(n)) <= "5" else "NOT!!"



# def special_number(number):
#     return "NOT!!" if any(x in set(str(number)) for x in "6789") else "Special!!"