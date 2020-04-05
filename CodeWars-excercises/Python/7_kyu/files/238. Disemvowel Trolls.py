def disemvowel(string):
    return ''.join(letter for letter in string if letter.lower() not in set('aeiou'))


# def disemvowel(s):
#     translator = str.maketrans({key: None for key in "aeiouAEIOU"})
#     return s.translate(translator)