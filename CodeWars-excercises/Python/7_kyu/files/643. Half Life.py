from datetime import datetime

def half_life(person1, person2):
    person1 = datetime.strptime(person1, '%Y-%m-%d')
    person2 = datetime.strptime(person2, '%Y-%m-%d')
    
    return datetime.strftime(max(person1, person2) + abs(person1 - person2), '%Y-%m-%d')



# from dateutil.parser import parse

# def half_life(*persons):
#     p1,p2 = sorted(map(parse, persons))
#     return str( p2+(p2-p1) )[:10]