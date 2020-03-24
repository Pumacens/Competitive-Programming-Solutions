from math import modf

def late_ride(n):
    seconds, hours = modf(n/60)
    num_string = str(int(hours)) +  str(int(round(seconds * 60, 2)))
    return sum(int(num) for num in num_string)



# def late_ride(n):
#     return sum([int(x) for x in (str(n % 60) + str(int(n / 60)))])