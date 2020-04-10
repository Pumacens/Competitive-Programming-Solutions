def segments(m, a):
    lst = []
    for num in range(m+1):
        num_in_some_segment = False
        
        for segment in a:
            if num in range(segment[0], segment[1]+1):
                num_in_some_segment = True
                break

        if not num_in_some_segment:
            lst.append(num)

    return lst
    


