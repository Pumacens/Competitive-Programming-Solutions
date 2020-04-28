def solution(digits):
    max_num = 0
    
    for i in range(len(digits)-4):
        num = int(digits[i:i+5]) 
        if num > max_num:
            max_num = num
            
    return max_num




# def solution(digits):
#     archivedVal = digits[:4]
#     for digit in range(len(digits)-4):
#         archivedVal = max(archivedVal, digits[digit:digit+5])
#     return int(archivedVal)