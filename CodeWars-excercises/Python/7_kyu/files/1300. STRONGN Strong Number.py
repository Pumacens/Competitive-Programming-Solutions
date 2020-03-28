from math import factorial as f
def strong_num(number):
    return "STRONG!!!!" if number == sum(f(int(digit)) for digit in str(number)) else "Not Strong !!"


# from math import factorial
# def strong_num(number):
#   return ("Not Strong !!", "STRONG!!!!")[sum(factorial(int(i)) for i in str(number)) == number]