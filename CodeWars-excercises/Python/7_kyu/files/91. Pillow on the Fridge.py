def pillow(s):
    return any(a=='n' and b=='B' for a,b in zip(s[0], s[1]))


# pillow=lambda s:('n','B') in zip(*s)