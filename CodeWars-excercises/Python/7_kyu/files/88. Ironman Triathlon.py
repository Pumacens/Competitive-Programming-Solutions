def i_tri(s):
#   Total distance  -> 140.6
    if not s:
        return 'Starting Line... Good Luck!'
        
    if s <=2.4:
        return {'Swim': f"{(140.6 - s):.2f} to go!"}
        
    if s <= 114.4:
        return {'Bike': f"{(140.6 - s):.2f} to go!"}
        
    if s <= 130.6:
        return {'Run': f"{(140.6 - s):.2f} to go!"}
        
    if s < 140.6:
        return {'Run': "Nearly there!"}
        
    else:
        return "You're done! Stop running!"


# def i_tri(s):
#     total = 2.4 + 112 + 26.2
#     to_go = '%.2f to go!' % (total - s)
#     return ( 'Starting Line... Good Luck!' if s == 0 else
#             {'Swim': to_go} if s < 2.4 else
#             {'Bike': to_go} if s < 2.4 + 112 else
#             {'Run':  to_go} if s < total - 10 else
#             {'Run': 'Nearly there!'} if s < total else
#             "You're done! Stop running!" )