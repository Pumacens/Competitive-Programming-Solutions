def growing_plant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = 0
    while True:
        height += upSpeed
        if height >= desiredHeight:
            return days
            
        height -= downSpeed
        days += 1



# from math import ceil

# def growing_plant(up, down, h):
#     return max(ceil((h - down) / (up - down)), 1)
