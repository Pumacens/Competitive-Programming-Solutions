def men_from_boys(arr):
    return sorted(dict.fromkeys(arr), key=lambda x: (x%2, -x if x%2 else x))



# def men_from_boys(arr):
#     men = []
#     boys = []
#     for i in sorted(set(arr)):
#         if i % 2 == 0:
#             men.append(i)
#         else:
#             boys.append(i)
#     return men + boys[::-1]




# def men_from_boys(arr):
#     odds, evens = [], []
#     for x in set(arr): [evens, odds][x%2].append(x)
#     return sorted(evens) + sorted(odds)[::-1]