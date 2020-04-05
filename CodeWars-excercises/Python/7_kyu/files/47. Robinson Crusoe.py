from math import (cos, sin, pi)

def crusoe(n, d, ang, dis_tmult, ang_mult):
    ang *= pi / 180
    points = [d*cos(ang), d*sin(ang)]
    
    for _ in range(n-1):
        d*= dis_tmult
        ang*= ang_mult
        
        points[0] += d * cos(ang)
        points[1] += d * sin(ang)
        
    return points



# def crusoe(n, d, ang, dis_tmult, ang_mult):
#     # your code
#     lastx=0
#     lasty=0
#     for i in range(n):
#         lastx += d*cos((ang*ang_mult**i)*pi/180)*dis_tmult**i
#         lasty += d*sin((ang*ang_mult**i)*pi/180)*dis_tmult**i
#     return (lastx, lasty)


