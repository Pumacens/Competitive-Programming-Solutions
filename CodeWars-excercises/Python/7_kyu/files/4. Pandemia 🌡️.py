def infected(s):
    if '1' not in s and '0' not in s:
        return 0

    s = ''.join(map(lambda cont: cont.replace('0', '1') if '1' in cont else cont,    s.split('X')))
    infected = s.count('1')
    total = infected + s.count('0')
    
    return infected / total * 100



# def infected(s):
#     lands = s.split('X')
#     total = sum(map(len, lands))
#     infected = sum(len(x) for x in lands if '1' in x)
#     return infected * 100 / (total or 1)



# import re

# def infected(s):
#     n = sum(map(len, re.findall(r'0*1[01]*', s)))
#     s = len(s.replace('X',''))
#     return s and 100*n/s



# def infected(s):
#     population = len(s) - s.count('X')
#     return population and 100 * sum(len(continent) for continent in s.split('X') if '1' in continent) / population