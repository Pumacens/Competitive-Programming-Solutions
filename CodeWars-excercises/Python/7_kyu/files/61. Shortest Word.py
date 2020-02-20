def find_short(s):
    return min(map(len, s.split(' ')))


# def find_short(s):
#     return min(len(x) for x in s.split())


# def find_short(s):
#     words=s.split()
#     short=len(words[0])
#     for word in words:
#         if short>len(word):
#             short=len(word)
#     return short


'''

I disagree. min() has O(n), this does not change because it is given an iterator as parameter(due to the fact, that (len(x) for x in s.split()) is a generator expression).

I wrote a simple benchmark that compares both versions discussed here as well as the "best practice" version with a generator expression replaced with a list comprehension.

https://codetidy.com/10143/

Result:

Number of Words	tanyaba's	best practice	list comprehension
10	5.7729994296096265e-06	8.289000106742606e-06	7.534999895142391e-06
100	2.8051001208950765e-05	3.284699960204307e-05	2.9044000257272273e-05
1000	0.00015123899902391713	0.00016145500012498815	0.00011981900024693459
10000	0.0010899510016315617	0.0013938470001448877	0.0011943779991270276
100000	0.012080994998541428	0.015169558999332367	0.013385842999923625
1000000	0.12315705000037269	0.15340965800169215	0.13438631999997597

'''