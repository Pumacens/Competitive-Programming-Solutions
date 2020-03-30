def absent_vowel(x): 
    return {
        'a' not in x: 0,
        'e' not in x: 1,
        'i' not in x: 2,
        'o' not in x: 3,
        'u' not in x: 4,
    }[True]
    
    

# def absent_vowel(x): 
#     return 'aeiou'.index((set('aeiou') - set(x.lower())).pop())