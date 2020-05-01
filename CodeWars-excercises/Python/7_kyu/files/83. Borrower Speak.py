import string
def borrow(s):
    return s.lower().translate(str.maketrans('', '', string.punctuation+' '))


# def borrow(s):
#     return ''.join(filter(str.isalpha, s.lower()))