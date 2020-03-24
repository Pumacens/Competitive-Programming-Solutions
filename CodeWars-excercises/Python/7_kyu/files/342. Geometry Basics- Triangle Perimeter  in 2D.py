from math import sqrt

def triangle_perimeter(triangle):
    a, b, c = triangle.a, triangle.b, triangle.c
    
    return (sqrt((a.x-b.x)**2 + (a.y-b.y)**2) + 
            sqrt((a.x-c.x)**2 + (a.y-c.y)**2) +
            sqrt((c.x-b.x)**2 + (c.y-b.y)**2) )



# from math import hypot

# def triangle_perimeter(t):
#     return sum(
#         hypot(p1.x-p2.x, p1.y-p2.y)
#         for p1, p2 in [(t.a,t.b),(t.b,t.c),(t.c,t.a)]
#     )



# from math import hypot
# from itertools import combinations

# def triangle_perimeter(t):
#     return sum(hypot(p.x-q.x,p.y-q.y) for p,q in combinations((t.a,t.b,t.c),2))