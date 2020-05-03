def solve(st):
    return max(st, key=lambda x: (abs(st.index(x) - st.rindex(x)), -ord(x)))


# def solve(st):
#     return min(set(st), key=lambda c: (st.index(c)-st.rindex(c), c))

