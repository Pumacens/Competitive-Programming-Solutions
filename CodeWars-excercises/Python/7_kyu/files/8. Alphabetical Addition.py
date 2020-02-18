import string

def add_letters( *letters ):
    dicc_letras = dict(zip(string.ascii_lowercase, range(1, len(string.ascii_lowercase)+1)))
    dicc_numeros = dict(zip(range(len(string.ascii_lowercase)), 'z' + string.ascii_lowercase))
    
    result_num = sum(dicc_letras[letter] for letter in letters)

    return dicc_numeros.get(result_num%26, 'z')



# num = 'abcdefghijklmnopqrstuvwxyz'
# def add_letters(*letters):
#     x = 0
#     x = sum(num.index(i)+1 for i in letters)
#     while x-1 > 25:
#         x -= 26
        
#     return num[x-1]



# def add_letters(*letters):
#     return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)