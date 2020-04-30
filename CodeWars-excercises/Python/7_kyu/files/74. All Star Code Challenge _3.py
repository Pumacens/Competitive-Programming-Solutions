def remove_vowels(strng):
    return ''.join(let for let in strng if let not in 'aeiou')



# REMOVE_VOWS = str.maketrans('','','aeiou')
# def remove_vowels(s):
#     return s.translate(REMOVE_VOWS)