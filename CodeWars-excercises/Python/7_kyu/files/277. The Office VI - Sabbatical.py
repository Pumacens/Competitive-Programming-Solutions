def sabb(s, value, happiness):
    final_value = value + happiness + sum(s.count(letter) for letter in 'sabticl')
    return 'Sabbatical! Boom!' if final_value > 22 else 'Back to your desk, boy.'



# def sabb(s, value, happiness):
#     return "Sabbatical! Boom!" if sum([sum(1 for i in s if i in "sabbatical"), value, happiness]) > 22 else "Back to your desk, boy."
