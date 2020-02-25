def hex_word_sum(string):
    string = string.replace('S', '5').replace('O', '0').split()
    
    def hex_to_decimal(word):
        try:
            return int(word, 16)
            
        except ValueError:
            return 0
            
    return sum(hex_to_decimal(word) for word in string)



# def hex_word_sum(s):
#     return sum(int(w, 16) for w in s.translate(str.maketrans('OS', '05')).split() if set(w) <= set('0123456789ABCDEF'))


# def hex_word_sum(s):
#   return sum(int(w, 16) for w in s.replace('O', '0').replace('S', '5').split() if all(c in '0123456789ABCDEF' for c in w))