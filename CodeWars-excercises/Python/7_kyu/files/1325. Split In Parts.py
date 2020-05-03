def split_in_parts(s, part_length): 
    return ' '.join(s[i*part_length:(i+1)*part_length] for i in range(0, len(s)//part_length+1)).strip()


# def split_in_parts(s, n): 
#     return ' '.join([s[i:i+n] for i in range(0, len(s), n)])


# from textwrap import wrap
# def split_in_parts(s, part_length): 
#     return " ".join(wrap(s,part_length))