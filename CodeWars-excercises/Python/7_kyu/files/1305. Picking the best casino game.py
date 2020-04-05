from operator import mul
from functools import reduce

def find_best_game(games):
    return max(games, key=lambda game: sum(map(lambda x: reduce(mul, x), game.outcomes))).name



# def find_best_game(games):
#     return max(games, key=lambda g: sum(odds * gain for odds, gain in g.outcomes)).name