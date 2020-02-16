def bonus_time(salary, bonus):
    return f'${salary * (10 if bonus else 1)}'


# def bonus_time(salary, bonus):
#     return '$' + str(salary * [1,10][bonus])