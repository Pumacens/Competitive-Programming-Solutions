def balanced_num(number):
    number = str(number)
    len_number = len(number)
    half_len = len_number//2
    
    if len_number < 3: return 'Balanced'
    
    return 'Balanced' if sum(map(int, number[:half_len - (len_number%2==0)])) == sum(map(int, number[half_len + 1:])) else "Not Balanced"
    

# def balancedNum(n):
#     s = str(n)
#     l = (len(s)-1)//2
#     same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
#     return "Balanced" if same else "Not Balanced"

# balanced_num = balancedNum