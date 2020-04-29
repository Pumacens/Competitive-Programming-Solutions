def binary_cleaner(seq): 
    ones = []
    greater_ones = []
    
    for indx, val in enumerate(seq):
        if val <= 1:
            ones.append(val)
            
        else:
            greater_ones.append(indx)
            
    return (ones, greater_ones)



# def binary_cleaner(seq): 
#     return list(filter(lambda x:x<=1, seq )), [ i for i in range(len(seq)) if seq[i]>1 ]