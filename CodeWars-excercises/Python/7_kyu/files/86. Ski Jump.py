def ski_jump(mountain):
    len_jump = len(mountain)**2 * 1.35
    return '{:.2f} metres: {}'.format(len_jump, ("He's crap!" if len_jump < 10 else "He's ok!" if 10 <= len_jump <= 25 else "He's flying!" if 25 < len_jump <= 50 else "Gold!!"))


# def ski_jump(mountain):
#     jump = len(mountain)**2 * 1.35
#     comment = "He's crap"   if jump < 10 else \
#               "He's ok"     if jump < 25 else \
#               "He's flying" if jump < 50 else \
#               "Gold!"
#     return f"{jump:.2f} metres: {comment}!"