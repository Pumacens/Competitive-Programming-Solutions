from math import ceil

def new_avg(arr, newavg):
    new_donation = newavg * (len(arr)+1) - sum(arr)
    
    if new_donation < 0:
        raise ValueError
        
    else:
        return ceil(new_donation)