import re
def is_letter(s):
    return bool(re.fullmatch(r'[a-zA-Z]', s))


# def is_letter(s):
#     return len(s) == 1 and s.isalpha()