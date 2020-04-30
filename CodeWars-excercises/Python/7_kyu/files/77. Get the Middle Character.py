def get_middle(s):
    len_s = len(s)
    if len_s <= 2:
        return s

    return s[len_s//2 - (len_s%2==0) : len_s//2 + 1]



# def get_middle(s):
#    return s[(len(s)-1)/2:len(s)/2+1]