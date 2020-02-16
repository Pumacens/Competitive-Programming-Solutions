import re

def is_lock_ness_monster(string):
    return bool(re.search(r'(three fifty|tree fiddy|3\.50)', string))


# def is_lock_ness_monster(s):
#     return any(i in s for i in ('tree fiddy', 'three fifty', '3.50'))


# def is_lock_ness_monster(s):
#     return bool(re.search(r'th?ree fi(?:dd|ft)y|3\.50', s))