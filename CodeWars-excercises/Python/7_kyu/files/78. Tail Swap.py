def tail_swap(strings):
    a,b =strings[0].split(':')
    c,d = strings[1].split(':')
    return [':'.join((a, d)) , ':'.join((c, b))]


