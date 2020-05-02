def testit(s):
    return ' '.join(map(lambda x: x[:-1] + x[-1].upper(),  s.split()))


# def testit(s):
#     return s[::-1].title()[::-1]



# import re
# def testit(s):
#     return re.sub(r'\w\b', lambda m: m.group().upper(), s)