def words_to_marks(s):
    return sum(ord(letter)-96 for letter in s)


# def words_to_marks(s):
#     return sum('_abcdefghijklmnopqrstuvwxyz'.index(e) for e in s)