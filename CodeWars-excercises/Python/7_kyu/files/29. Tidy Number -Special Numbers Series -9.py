def tidyNumber(n):
    digits = list(map(int, str(n)))
    actual_digit = digits[0]
    
    for digit in digits[1:]:
        if digit < actual_digit:
            return False
            
        actual_digit = digit
        
    return True
    

# def tidyNumber(n):
#     s = list(str(n))
#     return s == sorted(s)



# def tidyNumber(n):
#     return n == int(''.join(sorted(str(n))))


# def tidyNumber(n):
#     s = str(n)
#     return all(a<=b for a,b in zip(s,s[1:]))