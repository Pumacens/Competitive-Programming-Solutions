def map_vector(vector, circle1, circle2):
    vx, vy = vector
    cx_1, cy_1, cr_1 = circle1
    cx_2, cy_2, cr_2 = circle2
    
    proportion_x = cr_2 * abs(vx - cx_1) / cr_1
    proportion_y = cr_2 * abs(vy - cy_1) / cr_1
    
    print(proportion_x, proportion_y)
    
    if cx_1 > vx:
        if cy_1 > vy:
            return (cx_2 - proportion_x, cy_2 - proportion_y)
            
        else:
            return (cx_2 - proportion_x, cy_2 + proportion_y)
            
    else:
        if cy_1 > vy:
            return (cx_2 + proportion_x, cy_2 - proportion_y)
            
        else:
            return (cx_2 + proportion_x, cy_2 + proportion_y)
    
    


# def map_vector(vector, circle1, circle2):
#     x0, y0 = vector
#     x1, y1, r1 = circle1
#     x2, y2, r2 = circle2
#     scale = r2 / r1
#     return (
#         round(x2 + (x0-x1) * scale, 2),
#         round(y2 + (y0-y1) * scale, 2),
#     )