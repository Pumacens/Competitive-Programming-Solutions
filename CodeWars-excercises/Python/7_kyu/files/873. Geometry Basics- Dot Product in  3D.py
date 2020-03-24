def dot_product(a, b):
    return a.x*b.x + a.y*b.y + a.z*b.z


# def dot_product(a, b):
#     return sum(p * q for p, q in zip((a.x, a.y, a.z), (b.x, b.y, b.z)))


# def dot_product(a, b):
#     return sum(a.__getattribute__(c) * b.__getattribute__(c) for c in 'xyz')