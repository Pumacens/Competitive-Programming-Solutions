import re

def plane_seat(a):
    string = ''
    num = int(re.search(r'\d+', a).group(0))
    
    if 1 <= num <= 20:
        string += 'Front-'
        
    elif 21 <= num <= 40:
        string += 'Middle-'
        
    elif 41 <= num <= 60:
        string += 'Back-'
        
    elif num > 60:
        return 'No Seat!!'
        
    if bool(re.search(r'[A-C]', a)):
        return string + 'Left'
        
    elif bool(re.search(r'[D-F]', a)):
        return string + 'Middle'
        
    elif bool(re.search(r'[GHK]', a)):
        return string + 'Right'
        
    return 'No Seat!!'



# def plane_seat(s):
#     try:
#         a = int(s[:-1])
#         b = s[-1]
#         assert 1 <= a <= 60 and b not in "IJ"
#         return f"{'Front' if a < 21 else 'Middle' if a < 41 else 'Back'}-{'Left' if b <= 'C' else 'Middle' if b <= 'F' else 'Right'}"
#     except:
#         return "No Seat!!"

