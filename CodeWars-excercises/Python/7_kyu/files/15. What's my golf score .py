def golf_score_calculator(par_string, score_string):
    return sum(map(int, score_string)) - sum(map(int, par_string))


# def golf_score_calculator(par, score):
#     return sum(int(b) - int(a) for a, b in zip(par, score))


# def golf_score_calculator(p, s):
#     return sum([int(s[i])-int(p[i]) for i in range(len(p))])